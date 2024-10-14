<template>
  <div class="container w-full h-screen flex items-center justify-center">
    <Card class="w-[500px] shadow-lg md:shadow-xl">
      <CardHeader>
        <CardTitle class="text-center text-xl font-bold">Create Account</CardTitle>
        <CardDescription class="text-center">LGU MAYOYAO</CardDescription>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="register">
          <div class="grid items-center w-full gap-4">
            <div class="flex flex-col space-y-1.5">
              <Label for="name">Username</Label>
              <Input v-model="username" id="name" placeholder="Enter Username" required />
            </div>
            <div class="flex flex-col space-y-1.5">
              <Label for="email">Email</Label>
              <Input v-model="email" id="email" placeholder="Enter Email" required />
            </div>
            <div class="flex flex-col space-y-1.5">
              <Label for="password">Password</Label>
              <Input type="password" v-model="password" id="password" placeholder="Enter Password" required />
            </div>
            <div class="grid grid-cols-2 gap-1">
              <div class="flex flex-col col-span-1 space-y-1.5">
                <Label for="firstname">First Name</Label>
                <Input type="text" v-model="firstname" id="firstname" placeholder="Enter First Name" required />
              </div>
              <div class="flex flex-col col-span-1 space-y-1.5">
                <Label for="lastname">Last Name</Label>
                <Input type="text" v-model="lastname" id="lastname" placeholder="Enter Last Name" required />
              </div>
            </div>
            <div class="grid grid-cols-2 gap-1">
              <div class="flex flex-col col-span-1 space-y-1.5">
                <Label for="birthdate">Birthdate</Label>
                <Input class="w-36" type="date" v-model="birthdate" id="birthdate" required />
              </div>
              <div class="flex flex-col col-span-1 space-y-1.5 w-36">
                <Label for="sex">Sex</Label>
                <Select v-model="sex">
                  <SelectTrigger>
                    <SelectValue placeholder="Select sex" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="M">Male</SelectItem>
                    <SelectItem value="F">Female</SelectItem>
                    <SelectItem value="RNS">Rather not say</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
            <div class="flex justify-between">
              <Button
                type="submit"
                class="bg-orange-600 text-white px-4 py-2 rounded hover:bg-orange-700 transition"
              >
                Create Account
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
        </form>
      </CardContent>
    </Card>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const username = ref('')
const birthdate = ref('')
const sex = ref('')
const firstname = ref('')
const lastname = ref('')

const { $jwtAuth } = useNuxtApp()

async function register() {
  try {
    await $jwtAuth.signup(
      {
        username: username.value,
        first_name: firstname.value,
        last_name: lastname.value,
        email: email.value,
        birth_date: birthdate.value,
        gender: sex.value,
        password: password.value,
      },
      (data) => {
        console.log(data)
        window.location.replace('/')
      }
    )
  } catch (e) {
    // your error handling
  }
}

const goToLogin = () => {
  router.push('/login') // Replace with your desired route
}

definePageMeta({
  middleware: 'guest',
  layout: false
})
</script>
