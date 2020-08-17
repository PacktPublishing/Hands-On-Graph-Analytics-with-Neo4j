import React from 'react'
import { Link } from 'react-router-dom'
import { useQuery } from '@apollo/react-hooks'
import gql from 'graphql-tag'


const GET_USERS = gql`
  query Users {
    User {
      login
      email
      total_contributions
    }
  }
`

function UserList(props) {

  const { loading, data, error } = useQuery(GET_USERS);

  if (loading) {
    return <p>Loading...</p>
  }

  if (error !== undefined) {
    console.error(error);
    return <p>Error</p>
  }

  return (
      <table className={"table table-striped"}>
        <thead>
        <tr>
          <th>Login</th>
          <th>Email</th>
          <th>Total contributions</th>
        </tr>
        </thead>
        <tbody>
        {data.User.map((u) => {
          return (
              <tr key={u.login}>
                <td><Link to={`/user/${u.login}`}>{u.login}</Link></td>
                <td>{u.email}</td>
                <td>{u.totalContributions}</td>
              </tr>
          )
        })}
        </tbody>
      </table>
  )
};

export default UserList;
