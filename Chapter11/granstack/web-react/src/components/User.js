import React from 'react'
import { useQuery } from '@apollo/react-hooks'
import gql from 'graphql-tag'
import {Link} from "react-router-dom";


const GET_USER_DATA = gql`
query($login: String!) {
    User(login: $login) {
      owned_repositories {
        name
      }
   }
}
`;


function User(props) {

    let login = props.match.params.login;

    const { loading, data, error } = useQuery(GET_USER_DATA, {
        variables: {
            login: login
        }
    });

    if (loading) {
        return <p>Loading...</p>
    }

    if (error !== undefined) {
        return <p>Error: {error}</p>
    }

    let user = data.User[0];
    return (
        <ul>
            {user.owned_repositories.map((r) => {
                return (
                    <li key={r.name}>{r.name}</li>
                )
            })}
            <li><Link to={`/user/${login}/addrepo`}>Add new repository</Link></li>
        </ul>
    )
};

export {User, GET_USER_DATA};
