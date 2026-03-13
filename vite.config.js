import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        financials: resolve(__dirname, 'financials.html'),
        businessPlan: resolve(__dirname, 'business-plan.html'),
      }
    }
  }
})
