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

  const { $axios } = useNuxtApp()
    
  const users = ref()
  const title = ref('')
  const file = ref(null)
  const status = ref('')
  const assigned_to = ref('')
  const remarks = ref('')
  const document_type = ref('')
  const other_document_type = ref('')
  const from_person = ref()

  onMounted(async () => {
    try {
      const [usersResponse, dataResponse] = await Promise.all([
        $axios.get('users/'),
        $axios.get('user/')
      ]);

      users.value = usersResponse.data;
      from_person.value = dataResponse.data.id;

    } catch (err) {
      console.error('Error fetching data:', err);
    }
  });

  const {status_options, document_types} = selectStatusDocuType();

  const handleSave = async () => {
    const formData = new FormData();

    formData.append('title', title.value);
    formData.append('status', status.value);
    formData.append('assigned_to', assigned_to.value);
    formData.append('from_person', from_person.value);
    formData.append('document_type', document_type.value);
    formData.append('other_document_type', other_document_type.value);
    formData.append('remarks', remarks.value);

    if (file.value) {
      formData.append('file', file.value);
    }

    try {
      const response = await $axios.post('document/', formData, {
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
</script>
<template>
    <DialogContent class="sm:max-w-[500px]">
      <DialogHeader>
        <DialogTitle>Add new file</DialogTitle>
        <DialogDescription>
          Make sure to double check your file and file name to be uploaded
        </DialogDescription>
      </DialogHeader>
      <form class="grid gap-4 py-4" @submit.prevent="handleSave">
        <div class="grid grid-cols-4 items-center gap-1">
          <Label for="file_title" class="text-left">
            File Name
          </Label>
          <Input v-model="title" type="text" id="file_title" placeholder="Enter file name" class="col-span-4" />
        </div>
        <div class="grid grid-cols-4 items-center gap-1">
          <Label for="file" class="text-left">
            File
          </Label>
          <Input @change="e => file = e.target.files[0]" id="file" type="file" class="col-span-4" />
        </div>
        <div class="grid grid-cols-4 items-center gap-1">
          <!-- <div class="col-span-2">
            <Label for="status">Status</Label>
            <Select id="status" v-model="status">
              <SelectTrigger>
                <SelectValue placeholder="Select a status" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup v-for="data in status_options" :key=data.value>
                  <SelectItem :value=data.value>
                    {{data.display}}
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div> -->
          <div class="col-span-2">
            <Label for="assign">Assign To</Label>
            <Select id="assign" v-model="assigned_to">
              <SelectTrigger>
                <SelectValue placeholder="Select a user" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup v-for="data in users" :key=data.id>
                  <SelectItem :value="data.id.toString()">
                    {{data.username}}
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </div>
        </div>
        <div class="grid grid-cols-4 items-center gap-1">
          <Label for="document_type" class="col-span-4">Document Type</Label>
          <Select id="document_type" v-model="document_type">
            <SelectTrigger class="col-span-4">
              <SelectValue placeholder="Select a document type" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup v-for="data in document_types" :key=data>
                <SelectItem :value=data>
                  {{data}}
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div class="grid grid-cols-4 items-center gap-1">
          <Label for="other_document_type" class="col-span-4">Other Document Type</Label>
          <Input v-model="other_document_type" id="other_document_type" type="text" placeholder="Enter other document type" class="col-span-4" />
        </div>
        <div class="grid grid-cols-4 items-center gap-1">
          <Label for="remarks" class="col-span-4">Remarks</Label>
          <Input v-model="remarks" id="remarks" type="text" placeholder="Enter remarks" class="col-span-4" />
        </div>
        <DialogTrigger asChild>
          <Button type="submit">Submit</Button>
        </DialogTrigger>
      </form>
    </DialogContent>
  </template>