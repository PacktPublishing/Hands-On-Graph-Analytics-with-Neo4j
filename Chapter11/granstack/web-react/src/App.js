import React from 'react'
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'

import UserList from './components/UserList';
import {User} from './components/User'
import AddRepository from "./components/AddRepository";


export default function App() {
  return (
      <Router>
          <div>
              <h1><a href={"/"}>My app</a></h1>
          </div>

          <Switch>
              <Route exact path="/" component={UserList} />
              <Route path="/user/:login/addrepo" component={AddRepository} />
              <Route path="/user/:login" component={User} />
          </Switch>
      </Router>
  );
}
