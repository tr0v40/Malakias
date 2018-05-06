var  input = document.querySelectorAll('input[type="radio"]');
var approved = 0;
var canceled = 0;

function soma(value) {
    if (value == "Aprovado") {
        approved ++;
        console.log('ap',approved)
    } else{
        canceled ++;
        console.log('rp', canceled)
    }
       
}

function valid() {
    
    if (canceled + approved < 80){
        document.getElementById('save').type = 'reset';
        alert("Selecione todos os alunos.");    
        }
        else if(approved < 20)
        {
            document.getElementById('save').type = 'reset';
            alert("Minimo 20 alunos aprovados.");
        }
        else if(approved > 60)
        {
            document.getElementById('save').type = 'reset';
            alert("Máximo 60 alunos aprovados!");
    }
    else
    {
        document.getElementById('save').type = 'submit';
        alert("Enviado com sucesso!");
    }
    
};
