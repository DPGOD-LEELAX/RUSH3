<script setup lang="ts">
    import { ref, computed, onMounted } from 'vue'
    import AddFileDialog from '@/components/modals/file_manager/add-file.vue'
    import EditFileDialog from '@/components/modals/file_manager/edit-file.vue'
    import ViewFileDialog from '@/components/modals/file_manager/view-file.vue'
    import DeleteFileDialog from '@/components/modals/file_manager/delete-file.vue'
    import ApproveFileDialog from '@/components/modals/file_manager/approve-file.vue'
    import ArchiveFileDialog from '@/components/modals/file_manager/archive-file.vue'
    import moment from 'moment'
    definePageMeta({
        middleware: 'auth',
        layout:'default'
    })
    import {
        Table,
        TableBody,
        TableCaption,
        TableCell,
        TableHead,
        TableHeader,
        TableRow,
    } from '@/components/ui/table'

    import { 
        Dialog,
        DialogTrigger,
    } from '@/components/ui/dialog'

    import{
        Pencil,
        Trash2,
        Eye,
        Clock,
        Check,
        Loader,
        CheckCheck,
        CircleDashed,
        FileMinus,
        Archive,
        Printer // Import Printer icon for the print button
    } from 'lucide-vue-next'

    const filter = ref('')
    const searchTerm = ref('')

    const { $axios } = useNuxtApp()
    const files = ref()
    onMounted(async () => getDocuments());

    const getDocuments = async () => {
        try {
            const response = await $axios.get('document/')
            files.value = response.data
            console.log(response.data)
        } catch (err) {
            console.log(err)
        }
    }
    const getDocumentsPending = async () => {
        try {
            const response = await $axios.get('pending-document/')
            files.value = response.data
            console.log(response.data)
        } catch (err) {
            console.log(err)
        }
    }
    const getDocumentsDisabled = async () => {
        try {
            const response = await $axios.get('disabled-document/')
            files.value = response.data
            console.log(response.data)
        } catch (err) {
            console.log(err)
        }
    }
    const edit_id = ref()
    const setEditId = (value:number) => {
        edit_id.value = value
    }

    const filteredFiles = computed(() => {
        if (!files.value) return [];
        
        if (!searchTerm.value && filter.value === "") {
            return files.value.sort((a, b) => {
                return a.id - b.id;
            });
        }
        if (filter.value === 'recent') {
            return files.value.sort((a, b) => {
                return moment(b.uploaded_at).valueOf() - moment(a.uploaded_at).valueOf();
            });
        }
        if (filter.value !== '' && !searchTerm.value) {
            return files.value.filter(file =>
                file.status === filter.value
            )
        }
        if (searchTerm.value && filter.value !== ""){
            return files.value.filter(file =>
                file.reference_number.toString().toLowerCase().includes(searchTerm.value.toLowerCase()) && file.status == filter.value
            )
        }
        return files.value.filter(file =>
            file.title.toString().toLowerCase().includes(searchTerm.value.toLowerCase())
        )
    })

    const setFilter = (value:string) => {
        filter.value = value
        console.log(filter.value)
    }

    const handleSearch = () => {
        console.log('Searching for:', searchTerm.value)
    }
</script>

<template>
    <div class="flex items-center justify-between">
      <h1 class="text-lg font-semibold md:text-2xl">File Manager</h1>
    </div>
    <div class="flex mt-0 justify-between">
      <div class="w-full flex gap-4">
        <div class="flex w-full max-w-sm items-center gap-1.5">
          <Input id="email" type="email" v-model="searchTerm" placeholder="Search..." />
          <Button @click="handleSearch">Search</Button>
        </div>
      </div>
      <Dialog>
        <DialogTrigger>
          <Button class="bg-blue-500 text-white hover:bg-blue-600">Add new file</Button>
        </DialogTrigger>
        <AddFileDialog></AddFileDialog>
      </Dialog>
    </div>
    <div class="w-full">
      <div class="flex align-center">
        <Button variant="outline" class="mr-2 bg-gray-200 hover:bg-gray-300" @click='setFilter("")'>
          None
        </Button>
        <Button variant="outline" class="mr-2 bg-yellow-300 hover:bg-yellow-400" @click='setFilter("recent")'>
          <Clock class="w-4 h-4 mr-2" /> Recent
        </Button>
        <Button variant="outline" class="mr-2 bg-green-300 hover:bg-green-400" @click='setFilter("completed")'>
          <CheckCheck class="w-4 h-4 mr-2"/> Completed
        </Button>
        <Button variant="outline" class="mr-2 bg-blue-300 hover:bg-blue-400" @click='setFilter("in_progress")'>
          <CircleDashed class="w-4 h-4 mr-2" /> In Progress
        </Button>
        <Button variant="outline" class="mr-2 bg-purple-300 hover:bg-purple-400" @click='setFilter("archived")'>
          <Archive class="w-4 h-4 mr-2" /> Archived
        </Button>
        <Button variant="outline" class="mr-2 bg-green-500 text-white hover:bg-green-600" @click="getDocuments()">
          <Check class="w-4 h-4 mr-2" /> Approved
        </Button>
        <Button variant="outline" class="mr-2 bg-orange-300 hover:bg-orange-400" @click="getDocumentsPending()">
          <Loader class="w-4 h-4 mr-2" /> Pending
        </Button>
        <Button variant="outline" class="mr-2 bg-red-300 hover:bg-red-400" @click="getDocumentsDisabled()">
          <FileMinus class="w-4 h-4 mr-2" /> Disabled
        </Button>
      </div>
    </div>
    <div class="flex flex-1 justify-center rounded-lg border border-dashed shadow-sm">
      <Table>
        <TableCaption>A list of all the files stored in the database</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead class="w-[400px]">File Name</TableHead>
            <TableHead class="w-[150px]">Type</TableHead>
            <TableHead class="w-[150px]">Status</TableHead>
            <TableHead class="w-[200px]">Document Type</TableHead>
            <TableHead>Assigned To</TableHead>
            <TableHead>From</TableHead>
            <TableHead>Ref Num</TableHead>
            <TableHead class="w-[200px] text-center">Action</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="file in filteredFiles" :key="file.id">
            <TableCell class="font-medium">{{ file.title }}</TableCell>
            <TableCell>{{ file.file_type }}</TableCell>
            <TableCell>{{ file.status_display }}</TableCell>
            <TableCell>{{ file.document_type }}</TableCell>
            <TableCell>{{ file.to_username }}</TableCell>
            <TableCell>{{ file.from_username }}</TableCell>
            <TableCell>{{ file.reference_number }}</TableCell>
            <TableCell>
              <div class="flex justify-around gap-1">
                <Dialog>
                  <DialogTrigger>
                    <Button :key="file.id" @click="setEditId(file.id)" class="h-8 w-8 text-white bg-blue-600 hover:bg-blue-700" size="icon">
                      <Pencil />
                    </Button>
                  </DialogTrigger>
                  <EditFileDialog :key="file.id" :data="file.id"></EditFileDialog>
                </Dialog>
                <Dialog>
                  <DialogTrigger>
                    <Button @click="setEditId(file.id)" variant="destructive" class="h-8 w-8 bg-red-600 hover:bg-red-700" size="icon">
                      <Trash2 />
                    </Button>
                  </DialogTrigger>
                  <DeleteFileDialog :data="file.id"></DeleteFileDialog>
                </Dialog>
                <Dialog v-if="file.status === 'pending'">
                  <DialogTrigger>
                    <Button class="bg-green-400 text-white h-8 w-8 hover:bg-green-500" size="icon">
                      <Check />
                    </Button>
                  </DialogTrigger>
                  <ApproveFileDialog :data="file.id"></ApproveFileDialog>
                </Dialog>
                <Dialog>
                  <DialogTrigger>
                    <Button @click="setEditId(file.id)" class="bg-slate-400 text-white h-8 w-8 hover:bg-slate-500" size="icon">
                      <Archive />
                    </Button>
                  </DialogTrigger>
                  <ArchiveFileDialog :data="file.id"></ArchiveFileDialog>
                </Dialog>
                <Button @click="printDocument(file.id)" class="bg-purple-500 h-8 w-8 hover:bg-purple-600" size="icon">
                  <Printer />
                </Button>
                <!-- View Button -->
                <Dialog>
                  <DialogTrigger>
                    <Button @click="setEditId(file.id)" class="bg-green-500 h-8 w-8 hover:bg-green-600" size="icon">
                      <Eye />
                    </Button>
                  </DialogTrigger>
                  <ViewFileDialog :data="file.id"></ViewFileDialog>
                </Dialog>
              </div>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
</template>
