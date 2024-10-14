import axios from 'axios'

export default defineNuxtPlugin((nuxtApp) => {
  const instance = axios.create({
    baseURL: 'http://localhost:8000/api/',
  })

  instance.interceptors.request.use((config) => {
    const {token} = useJwtAuth()

    if (token) {
      config.headers.Authorization = `Bearer ${token.value}`
    }

    return config
  })

  return {
    provide: {
      axios: instance,
    },
  }
})