import Vue from 'vue'
import Router from 'vue-router'
import listJuego from '@/components/juego/listJuego'
import createJuego from '@/components/juego/createJuego'
import EditJuego from '@/components/juego/EditJuego'
import deleteJuego from '@/components/juego/deleteJuego'
import detailJuego from '@/components/juego/detailJuego'
//

import register from '@/components/user/register'
import login from '@/components/user/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'listJuego',
      component: listJuego
    },
    {
      path: '/create',
      name: 'createJuego',
      component: createJuego
    },
    {
      path: '/juego/edit/:juegoId',
      name: 'EditJuego',
      component: EditJuego
    },
    {
      path: '/juego/delete/:juegoId',
      name: 'deleteJuego',
      component: deleteJuego
    },
    {
      path: '/juego/detail/:juegoId',
      name: 'detailJuego',
      component: detailJuego
    },
    //users routers
    {
      path: '/SingUp',
      name: 'register',
      component: register
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },

  ],
  mode: 'history'
})
