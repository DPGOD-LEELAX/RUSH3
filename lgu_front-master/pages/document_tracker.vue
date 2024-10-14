<!-- <template>
  <div class="container w-full h-screen flex-col gap-4 flex items-center justify-center">
    <Card class="w-[350px] shadow-lg md:shadow-xl">
      <CardHeader>
        <CardTitle>LGU MAYOYAO</CardTitle>
        <CardDescription>Document Tracker</CardDescription>
      </CardHeader>
      <CardContent>
        <div class="grid items-center w-full gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="ref_num">Reference Number</Label>
            <Input v-model="ref_num" type="text" id="ref_num" placeholder="Enter reference number" required />
          </div>
          <div class="flex justify-between">
            <Button
              type="button"
              @click="queryDocument()"
              class="bg-orange-600 text-white px-4 py-2 rounded hover:bg-orange-700 transition"
            >
              Track
            </Button>
            <Button
              type="button"
              @click="goToLogin"
              class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
            >
              Go to Login
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
    
    <Card class="w-[350px] shadow-lg md:shadow-xl" v-if="file.title">
      <CardHeader>
        <CardTitle>Document Found</CardTitle>
        <CardDescription>Document</CardDescription>
      </CardHeader>
      <CardContent>
        <div class="grid items-center w-full gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="ref_num">File Name</Label>
            <Input v-model="file.title" type="text" id="file_name" placeholder="Enter reference number" readonly />
          </div>
          <div class="flex flex-col space-y-1.5">
            <Label for="ref_num">Status</Label>
            <Input v-model="file.status_display" type="text" id="status" placeholder="Enter reference number" readonly />
          </div>
        </div>
      </CardContent>
    </Card>

  
    <div v-if="showErrorModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="bg-white rounded-lg p-6 shadow-lg w-[300px] text-center">
        <h2 class="text-lg font-semibold text-red-600">Error</h2> 
        <p class="mt-2 text-black-600">Invalid reference number. Please try again.</p> 
        <Button type="button" @click="closeErrorModal" variant="outline" class="mt-4">Close</Button>
      </div>
    </div>

  </div>
</template>

<script setup>
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Button } from '@/components/ui/button'
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const ref_num = ref('')
const file = ref({})
const showErrorModal = ref(false) 
const router = useRouter()

const goToLogin = () => {
  router.push({ name: 'login' }) 
}

const queryDocument = async () => {
  file.value = {}
  showErrorModal.value = false 
  try {
    const response = await axios.get(`http://localhost:8000/api/get-document/${ref_num.value}/`)
    if (response.status === 200) {
      file.value = response.data
    }
  } catch (err) {
    if (err.response && err.response.status === 404) {
      showErrorModal.value = true 
    } else {
      console.log(err)
    }
  }
}

const closeErrorModal = () => {
  showErrorModal.value = false 
}

definePageMeta({
  middleware: 'guest',
  layout: false
})
</script>
 -->







 <template>
  <div class="container w-full h-screen flex-col gap-4 flex items-center justify-center bg-cover bg-center bg-no-repeat" style="background-image: url('/logbg.png');"> <!-- Updated the URL to point to the public folder -->
    <Card class="w-[890px] shadow-lg md:shadow-xl bg-white"> <!-- Added bg-white for card isolation -->
      <CardHeader class="flex flex-col items-center">
        <CardTitle class="text-center font-mono">ONLINE DOCUMENT TRACKING SYSTEM</CardTitle>
      </CardHeader>

      <CardContent>
        <div class="flex items-center w-full gap-4"> 
          <div class="flex-grow">
            <Input
              v-model="ref_num"
              type="text"
              id="ref_num"
              placeholder="Enter reference number"
              required
            />
          </div>
          <Button
            type="button"
            @click="queryDocument()"
            class="bg-orange-600 text-white px-4 py-2 rounded hover:bg-orange-700 transition"
          >
            Track
          </Button>
        </div>
        <div class="flex justify-between mt-4">
          <Button
            type="button"
            @click="goToLogin"
            class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
          >
            Go to Login
          </Button>
        </div>
      </CardContent>
    </Card>

    <Card class="w-[350px] shadow-lg md:shadow-xl bg-white" v-if="file.title"> <!-- Added bg-white for isolation -->
      <CardHeader>
        <CardTitle>Document Found</CardTitle>
        <CardDescription>Document</CardDescription>
      </CardHeader>
      <CardContent>
        <div class="grid items-center w-full gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="ref_num">File Name</Label>
            <Input v-model="file.title" type="text" id="file_name" placeholder="Enter reference number" readonly />
          </div>
          <div class="flex flex-col space-y-1.5">
            <Label for="ref_num">Status</Label>
            <Input v-model="file.status_display" type="text" id="status" placeholder="Enter reference number" readonly />
          </div>
        </div>
      </CardContent>
    </Card>

    <div v-if="showErrorModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="bg-white rounded-lg p-6 shadow-lg w-[300px] text-center">
        <h2 class="text-lg font-semibold text-red-600">Error</h2>
        <p class="mt-2 text-black-600">Invalid reference number. Please try again.</p>
        <Button type="button" @click="closeErrorModal" variant="outline" class="mt-4">Close</Button>
      </div>
    </div>
  </div>
</template>




<script setup>
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Button } from '@/components/ui/button'
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const ref_num = ref('')
const file = ref({})
const showErrorModal = ref(false) 
const router = useRouter()

const goToLogin = () => {
  router.push({ name: 'login' }) 
}

const queryDocument = async () => {
  file.value = {}
  showErrorModal.value = false 
  try {
    const response = await axios.get(`http://localhost:8000/api/get-document/${ref_num.value}/`)
    if (response.status === 200) {
      file.value = response.data
    }
  } catch (err) {
    if (err.response && err.response.status === 404) {
      showErrorModal.value = true 
    } else {
      console.log(err)
    }
  }
}

const closeErrorModal = () => {
  showErrorModal.value = false 
}

definePageMeta({
  middleware: 'guest',
  layout: false
})
</script> 



<style>
</style>









