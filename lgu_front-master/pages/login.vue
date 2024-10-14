<template>
  <div class="container w-full h-screen flex items-center justify-center">
    <Card class="w-full max-w-[350px] shadow-2xl border border-black-100 bg-card-background rounded-2xl">
      <CardHeader class="flex flex-col items-center">
        <img :src="imgSRC" alt="Logo" class="w-44 h-44 mb-4 logo-shadow font-serif" />
        <CardTitle class="text-shadow font-mono">LGU MAYOYAO</CardTitle>
        <CardDescription class="text-shadow text-black font-serif">Please Log In</CardDescription>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="login">
          <div class="grid items-center w-full gap-4">
            <div class="flex flex-col space-y-1.5">
              <Label for="name" class="text-shadow">Email</Label>
              <Input v-model="email" id="name" placeholder="Enter Email" required class="input-shadow" />
            </div>
            <div class="flex flex-col space-y-1.5">
              <Label for="password" class="text-shadow">Password</Label>
              <Input type="password" v-model="password" id="password" placeholder="Enter Password" required class="input-shadow" />
            </div>
            <div class="flex flex-col w-full space-y-2">
              <Button
                type="submit"
                class="w-full bg-blue-600 text-white font-serif py-3 rounded-lg shadow-md hover:bg-blue-700 transition duration-300 btn-shadow"
              >
                <i class="fas fa-sign-in-alt mr-2"></i> Login
              </Button>
              <Button
                type="button"
                @click="goToRegister"
                class="w-full bg-green-600 text-white font-serif py-3 rounded-lg shadow-md hover:bg-green-700 transition duration-300 btn-shadow"
              >
                <i class="fas fa-user-plus mr-2"></i> Create Account
              </Button>
            </div>
          </div>
        </form>
      </CardContent>
      <CardFooter class="flex justify-center px-6 pb-6">
        <Button
          type="button"
          @click="goToTracker"
          class="w-full bg-gray-600 text-white font-serif py-3 rounded-lg shadow-md hover:bg-gray-700 transition duration-300 btn-shadow"
        >
          <i class="fas fa-file-alt mr-2"></i> Document Tracker
        </Button>
      </CardFooter>
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
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import imgSRC from '@/public/logo.png'

const router = useRouter()

const email = ref('');
const password = ref('');

const { $jwtAuth } = useNuxtApp()

async function login() {
  try {
    await $jwtAuth.login(
      {
        email: email.value,
        password: password.value
      },
      (data) => {
        console.log(data)
        window.location.replace('/')
      }
    )
  } catch (e) {
    // Handle error
  }
}

const goToRegister = () => {
  router.push('/register') 
}

const goToTracker = () => {
  router.push('/document_tracker') 
}

definePageMeta({
  middleware: 'guest',
  layout: false
})
</script>

<style scoped>
.container {
  background-color: white; 
}

.bg-card-background {
  background-image: url('/public/logbg.png');
  background-size: cover;
  background-position: center;
}

.text-shadow {
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.6);
}

.input-shadow {
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.4);
}

.btn-shadow {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.6);
}


</style>
