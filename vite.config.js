import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        product: resolve(__dirname, 'product.html'),
        market: resolve(__dirname, 'market.html'),
        businessModel: resolve(__dirname, 'business-model.html'),
        team: resolve(__dirname, 'team.html'),
        roadmap: resolve(__dirname, 'roadmap.html'),
        invest: resolve(__dirname, 'invest.html'),
        financials: resolve(__dirname, 'financials.html'),
        azMain: resolve(__dirname, 'az/index.html'),
        azProduct: resolve(__dirname, 'az/product.html'),
        azMarket: resolve(__dirname, 'az/market.html'),
        azBusinessModel: resolve(__dirname, 'az/business-model.html'),
        azTeam: resolve(__dirname, 'az/team.html'),
        azRoadmap: resolve(__dirname, 'az/roadmap.html'),
        azInvest: resolve(__dirname, 'az/invest.html'),
        azFinancials: resolve(__dirname, 'az/financials.html'),
      }
    }
  }
})
