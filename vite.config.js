import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        solution: resolve(__dirname, 'solution.html'),
        product: resolve(__dirname, 'product.html'),
        market: resolve(__dirname, 'market.html'),
        businessModel: resolve(__dirname, 'business-model.html'),
        traction: resolve(__dirname, 'traction.html'),
        team: resolve(__dirname, 'team.html'),
        roadmap: resolve(__dirname, 'roadmap.html'),
        invest: resolve(__dirname, 'invest.html'),
        financials: resolve(__dirname, 'financials.html'),
        businessPlan: resolve(__dirname, 'business-plan.html'),
      }
    }
  }
})
