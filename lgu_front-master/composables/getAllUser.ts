export async function getAllUsers(){
    const { $axios } = useNuxtApp()
    try {
        const response = await $axios.get(`users/`);
        return response.data
    } catch (err) {
        console.error('Error submitting the form:', err);
        return []
    }
}