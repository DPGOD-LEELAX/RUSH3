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

  const {document_types} = selectStatusDocuType();

  const { $axios } = useNuxtApp()

  const title = ref('')
  const document_type = ref('')
  const other_document_type = ref('')

  const handleSave = async () => {
    const formData = new FormData();

    formData.append('title', title.value);
    formData.append('document_type', document_type.value);
    formData.append('other_document_type', other_document_type.value);
    formData.append('status', "in_progress")

    try {
      const response = await $axios.put(`edit-document/${props.data}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      window.location.reload();
    } catch (err) {
      console.error('Error submitting the form:', err);
    }
  };

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
      // console.log(response.data);
      passData(response.data)
    } catch (err) {
      console.error('Error submitting the form:', err);
    }
  }

  const passData = (file) => {
    title.value = file.title
    document_type.value = file.document_type
    other_document_type.value = file.other_document_type
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
      <DialogTitle>Approve File</DialogTitle>
      <DialogDescription>
        Are you sure you want to approve this file?
      </DialogDescription>
    </DialogHeader>
    <form class="grid gap-4 py-4" @submit.prevent="handleSave">
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="file_title" class="text-left">
          File Name
        </Label>
        <Input v-model="title" type="text" id="file_title" placeholder="Enter file name" class="col-span-4" readonly/>
      </div>
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="document_type" class="col-span-4">Document Status</Label>
        <Select id="document_type" v-model="document_type" :disabled="true">
          <SelectTrigger class="col-span-4">
            <SelectValue placeholder="Select a document type" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup v-for="data in document_types" :key=data>
              <SelectItem :value="data">
                {{data}}
              </SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      <div class="grid grid-cols-4 items-center gap-1">
        <Label for="other_document_type" class="col-span-4">Other Document Type</Label>
        <Input v-model="other_document_type" id="other_document_type" type="text" placeholder="Enter other document type" class="col-span-4" readonly/>
      </div>
      <DialogTrigger asChild>
        <Button type="submit">Submit</Button>
      </DialogTrigger>
    </form>
  </DialogContent>
</template>