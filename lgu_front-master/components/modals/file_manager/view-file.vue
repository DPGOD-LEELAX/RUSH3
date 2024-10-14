<script setup lang = "ts">   
  import { ref } from 'vue';
  import {
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
  } from '@/components/ui/dialog'
  import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue,
  } from '@/components/ui/select'

  const {status_options, document_types} = selectStatusDocuType();

  const { $axios } = useNuxtApp()
    
  const users = ref()
  const title = ref('')
  const status = ref('')
  const remarks = ref('')
  const to_username = ref('')
  const from_username = ref('')
  const document_type = ref('')
  const other_document_type = ref('')
  const from_person = ref()

  onMounted(async () => {
    try {
      // Execute both requests concurrently
      const [usersResponse, dataResponse] = await Promise.all([
        $axios.get('users/'),
        $axios.get('user/')
      ]);

      // Update refs with the response data
      users.value = usersResponse.data;
      from_person.value = dataResponse.data.id;
    } catch (err) {
      console.error('Error fetching data:', err);
    }
  });

    // Modal Handling
  const props = defineProps<{
    data: number
  }>();
    
  const getDocumentData = async (data:number) => {
    try {
      const response = await $axios.get(`document/${data}/`, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      passData(response.data)
    } catch (err) {
      console.error('Error submitting the form:', err);
    }
  }

  const passData = (file) => {
    title.value = file.title
    status.value = file.status_display
    from_person.value = from_person.value
    document_type.value = file.document_type
    other_document_type.value = file.other_document_type
    remarks.value = file.remarks
    to_username.value = file.to_username
    from_username.value = file.from_username
  }
  watchEffect(() => {
  if (props.data) {
    console.log(props.data)
    getDocumentData(props.data);
  }
});

</script>
<template>
  <DialogContent class="sm:max-w-[500px]">
    <DialogHeader>
      <DialogTitle>View File Info</DialogTitle>
      <DialogDescription>
        This shows the full information of the document
      </DialogDescription>
    </DialogHeader>
    <form class="grid gap-4 py-4">
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="file_title" class="text-left">
          File Name
        </Label>
        <Input v-model="title" type="text" id="file_title" class="col-span-4" readonly/>
      </div>
      <div class="grid grid-cols-4 items-center gap-1">
        <div class="col-span-2">
          <Label for="status">Status</Label>
          <Input v-model="status" id="remarks" type="text" class="col-span-4" readonly/>
        </div>
        <div class="col-span-2">
          <Label for="assign">Assign To</Label>
          <Input v-model="to_username" id="remarks" type="text" class="col-span-4" readonly/>
        </div>
      </div>
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="document_type" class="col-span-4">Document Type</Label>
        <Input v-model="document_type" id="remarks" type="text" class="col-span-4" readonly/>
      </div>
      <div class="grid grid-cols-4 items-center gap-1" v-if="other_document_type">
        <Label for="other_document_type" class="col-span-4">Other Document Type</Label>
        <Input v-model="other_document_type" id="other_document_type" type="text" placeholder="Enter other document type" class="col-span-4" readonly/>
      </div>
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="remarks" class="col-span-4">Remarks</Label>
        <Input v-model="remarks" id="remarks" type="text" placeholder="Enter remarks" class="col-span-4" readonly/>
      </div>
      <DialogTrigger asChild>
        <Button>Close Modal</Button>
      </DialogTrigger>
    </form>
  </DialogContent>
</template>