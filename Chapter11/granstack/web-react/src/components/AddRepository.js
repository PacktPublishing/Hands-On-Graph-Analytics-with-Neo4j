import React from "react";
import { useMutation } from '@apollo/react-hooks';
import gql from "graphql-tag";
import {GET_USER_DATA} from './User';


const CREATE_REPO = gql`
mutation($name: String!, $login: String!) {
  CreateRepository(name: $name) {
    name
  }
  AddRepositoryOwner(from: { login: $login }, to: { name: $name }) {
    from {
      login
    }
    to {
      name
    }
  }
}
`;



function AddRepository(props) {
    let login = props.match.params.login;

    const [mutation, ] = useMutation(CREATE_REPO);

    const submitForm = function(e) {
        e.preventDefault();
        mutation({variables: {
                login: login,
                name: e.target.name.value,
            },
        refetchQueries: [{query: GET_USER_DATA, variables: {login: login}}]});
        props.history.push(`/user/${login}`);
    };


    return (
        <form onSubmit={submitForm}>
            <input type={"test"} name={"name"} placeholder={"New repository name"}/>
            <input type={"submit"}/>
        </form>
    )
}

export default AddRepository;
