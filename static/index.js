
const checkBox=document.querySelectorAll('#flexCheckDefault')
        
for(let box of checkBox)
{
   box.addEventListener('change',async()=>{
     
      await fetch(`/doneTask/${box.value}`)
      window.location.href='/'

   })
}