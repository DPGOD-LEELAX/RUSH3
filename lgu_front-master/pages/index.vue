<script setup lang="ts">
import {ref, onMounted} from 'vue'
import { DonutChart } from '@/components/ui/chart-donut'
import { BarChart } from '@/components/ui/chart-bar'

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'

import { 
  UsersRound,
  FilePenLine,
  FileDown,
  FileUp,
  File,
  CircleUserRound,
  Files,
  FileStack
} from 'lucide-vue-next'

import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

import {getAllUsers} from '~/composables/getAllUser'


const data = [
  { name: 'Jan', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Feb', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Mar', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Apr', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'May', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Jun', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Jul', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Aug', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Sep', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Oct', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Nov', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
  { name: 'Dec', downloads: Math.floor(Math.random() * 5000) + 1000, uploads: Math.floor(Math.random() * 3000) + 500 },
]


definePageMeta({
  middleware: 'auth',
  layout:'default'
})
const { $axios } = useNuxtApp()
const user_count = ref({
  user_count: 0
})

const users = ref({
  id: 0,
  username: ''
})

const document_status_count = ref({
  total_docuents: 0,
  status_counts: []
})

onMounted(async () => {
  await getUserCount()
  await getDocumentStatusCount()
  users.value = await getAllUsers()
  console.log(users.value)
})

const getUserCount = async () => {
  try {
    const response = await $axios.get('user-count/')
    user_count.value = response.data
    console.log(response.data)
  } catch (err) {
    console.log(err)
  }
}
const getDocumentStatusCount= async () => {
  try {
    const response = await $axios.get('get-document-count/')
    document_status_count.value = response.data
    console.log(document_status_count.value)
  } catch (err) {
    console.log(err)
  }
}

</script>
<template>
  <div class="flex flex-col items-start">
    <h1 class="text-2xl font-bold md:text-4xl">
      DOCUMENT TRACKING AND FILING SYSTEM
    </h1>
    <h2 class="text-lg font-semibold md:text-2xl mt-6">
      Dashboard
    </h2>
  </div>
  <div class="flex flex-1 gap-4 p-5 rounded-lg border border-dashed shadow-sm grid grid-cols-8 bg-gray-50">
    <div class="grid grid-cols-subgrid gap-4 col-span-8">
      <div class="col-span-2">
        <Card class="drop-shadow-md">
          <CardHeader>
            <CardTitle class="flex items-center gap-4"><Button size="icon"><FileStack class="w-8 h-8"/></Button>Document Count</CardTitle>
            <CardDescription>This shows document count based on status</CardDescription>
          </CardHeader>
          <CardContent>
            <DonutChart
              index="name"
              :category="'count'"
              :data="document_status_count.status_counts"
              :colors="['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']"
            />
          </CardContent>
        </Card>
      </div>
      <div class="col-span-2">
        <Card class="drop-shadow-md h-full">
          <CardHeader>
            <CardTitle class="flex items-center gap-4"><Button size="icon"><CircleUserRound class="w-8 h-8"/></Button>Total Users</CardTitle>
            <CardDescription>This shows number of users</CardDescription>
          </CardHeader>
          <CardContent class="text-3xl font-bold flex items-center gap-4 justify-center">
            <UsersRound class="w-12 h-12"/>
            {{ user_count.user_count }}
          </CardContent>
        </Card>
      </div>
      <div class="col-span-4">
        <Card class="drop-shadow-md h-full">
          <CardHeader>
            <CardTitle class="flex gap-4 items-center"><Button size="icon"><FilePenLine class="w-8 h-8"/></Button>Latest Document Update</CardTitle>
            <CardDescription>This shows the latest update on a document</CardDescription>
          </CardHeader>
          <CardContent>
            <Card>
              <CardContent class="flex items-center mt-5 font-medium gap-4">
                <File class="w-6 h-6"/> Document Name
              </CardContent>
            </Card>
          </CardContent>
        </Card>
      </div>
    </div>
    <div class="col-span-4">
      <Card class="drop-shadow-md">
          <CardHeader>
            <CardTitle class="flex gap-4 items-center"><Button size="icon"><FileUp class="w-8 h-8"/></Button>Latest Document Uploaded</CardTitle>
            <CardDescription>This shows the most recent uploaded document</CardDescription>
          </CardHeader>
          <CardContent>
            <Card>
              <CardContent class="flex items-center mt-5 font-medium gap-4">
                <File class="w-6 h-6"/> Document Name
              </CardContent>
            </Card>
          </CardContent>
        </Card>
    </div>
    <div class="col-span-4">
      <Card class="drop-shadow-md">
          <CardHeader>
            <CardTitle class="flex gap-4 items-center"><Button size="icon"><FileDown class="w-8 h-8"/></Button>Latest Document Downloaded</CardTitle>
            <CardDescription>This shows the most recent downloaded document</CardDescription>
          </CardHeader>
          <CardContent>
            <Card>
              <CardContent class="flex items-center mt-5 font-medium gap-4">
                <File class="w-6 h-6"/> Document Name
              </CardContent>
            </Card>
          </CardContent>
        </Card>
    </div>
    <div class="col-span-8">
      <Card class="drop-shadow-md">
        <CardHeader>
          <CardTitle class="flex items-center gap-4"><Button size="icon"><Files class="w-8 h-8"/></Button>Total Document Upload and Download</CardTitle>
          <CardDescription>This shows number of uploads and downloads on a monthly basis</CardDescription>
        </CardHeader>
        <CardContent class="flex justify-center">
            <BarChart
              :data="data"
              index="name"
              :categories="['downloads', 'uploads']"
              :y-formatter="(tick, i) => {
                return typeof tick === 'number'
                  ? `${new Intl.NumberFormat('us').format(tick).toString()}`
                  : ''
              }"
              :rounded-corners="4"
              :colors="['red','blue']"
              :show-x-axis="true"
            />
        </CardContent>
      </Card>
    </div>
    <div class="col-span-2">
      <Card class="drop-shadow-md">
      <CardHeader>
        <CardTitle class="flex items-center gap-4">
          <Button size="icon">
            <CircleUserRound class="w-8 h-8" />
          </Button>
          Active Users
        </CardTitle>
      </CardHeader>
      <CardContent>
        <Table>
          <TableCaption>A list of active users</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead class="w-[150px]">Username</TableHead>
              <TableHead class="w-[150px]">Action</TableHead> <!-- Add Action Column -->
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow v-for="data in users" :key="data.id">
              <TableCell>{{ data.username }}</TableCell>
              <TableCell>
                <!-- Edit Button -->
                <Button variant="secondary" size="sm" @click="editUser(data.id)">
                  Edit
                </Button>
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </CardContent>
    </Card>

    </div>
  </div>
</template>