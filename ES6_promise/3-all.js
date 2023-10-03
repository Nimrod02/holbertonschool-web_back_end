import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((result) => {
      console.log(`${result[0].body}, ${result[0].firstname}, ${result[1].createUser}`);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
