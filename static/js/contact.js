const btnContact = document.getElementById('btn-contact');

document.getElementById('contact-form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btnContact.value = 'Sending...';

   const serviceID = 'service_tojv94i';
   const templateID = 'askjapanese_contact';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btnContact.value = 'Send Email';
      alert('Sent!');
    }, (err) => {
      btnContact.value = 'Send Email';
      alert(JSON.stringify(err));
    });
});