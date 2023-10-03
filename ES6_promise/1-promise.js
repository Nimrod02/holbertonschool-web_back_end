const status = 200;
const body = 'sucess';
const error = 'The fake API is not working currently';

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status, body });
    } else {
      reject(new Error(error));
    }
  });
}
