import React from 'react';

const Profile = props => {
    return (
        <div>
            <h3>Name: {props.name}</h3>
            <p>Profession: {props.profession}</p>
            <button onClick={props.logoutHandlar} className="btn btn-danger btn-sm">Logout</button>
        </div>
    );
}

export default Profile;
