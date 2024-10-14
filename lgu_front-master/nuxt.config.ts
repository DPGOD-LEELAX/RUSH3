// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  plugins: ['~/plugins/axios.js'],
  modules: [
    '@nuxtjs/tailwindcss',
    'shadcn-nuxt',
    "@nuxt/eslint",
    'nuxt-jwt-auth',
  ],
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },
  nuxtJwtAuth: {
    baseUrl: 'http://localhost:8000/api/', // URL of your backend
    endpoints: {
      login: 'login/', // Where to request login (POST)
      logout: 'logout/', // Where to request logout (POST)
      user: 'user/', // Where to request user data (GET)
      signup: 'register/' // Where to request signup (POST)
    },
    redirects: {
      home: '/', // Where to redirect after successfull login and logout
      login: '/login', // Where to redirect if user is not logged in and accesses a logged-only route
      logout: '/logout' // Where to redirect if user is logged in and accesses a guest-only route 
    }
  },
  css: [
    '@/assets/css/tailwind.css',
  ]
})