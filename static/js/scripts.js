const $range = document.getElementById("range")
const $lblrange = document.getElementById('lblrange')
const $checks = document.querySelectorAll('.check')
const $vweak = document.querySelector('.vweak')
const $weak = document.querySelector('.weak')
const $medium = document.querySelector('.medium')
const $strong = document.querySelector('.strong')
const $copyPass = document.querySelector('#passw.copy')

let rngValue = $range.value
let numChars = $range.value
let optsPoints = 0
$lblrange.textContent = 'Nº de caracteres: '+$range.value

$range.addEventListener("pointermove", (e) =>{
    $lblrange.textContent = 'Nº de caracteres: '+$range.value
})


$range.addEventListener('change', (e) =>{
    $lblrange.textContent = 'Nº de caracteres: '+$range.value
    let actValue = parseInt($range.value)
    
    if (rngValue > actValue){
        let tmpNum = numChars - actValue
        numChars+=tmpNum
    }else{
        let tmpNum = numChars - actValue
        numChars-=tmpNum
    }

    strenghValue()
})

$checks.forEach(el => {
    el.addEventListener("change", e =>{
        if (el.checked === false){
            optsPoints-=0.5
        } else{
            optsPoints+=0.5
        }
        strenghValue()
    })
});

const strenghValue = () =>{

    document.querySelectorAll('.lvl').forEach(el =>{
        if (el.classList.contains('on')){
            el.classList.toggle('on')
        }        
    })

    if (optsPoints>0){
        let strengh = parseInt(numChars)+parseInt(optsPoints)
        
        if(strengh > 2){
            $vweak.classList.add("on")
        }
        if(strengh > 5){
            $weak.classList.add("on")
        }
        if(strengh > 8){
            $medium.classList.add("on")
        }
        if(strengh > 9){
            $strong.classList.add("on")
        }
    }
}

if($copyPass!=null){
    $copyPass.addEventListener("click", async () =>{
        try{
            await navigator.clipboard.writeText($copyPass.textContent.trim());
            alert("Contraseña copiada al portapapeles")
        } catch(err){
            alert("Error: ", err )
        }
        
    })
}