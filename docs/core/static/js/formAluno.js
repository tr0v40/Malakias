function validacao() {
    /*Valida senhas */
    var password = document.getElementById("senha");
    var confirm_password = document.getElementById("confirma_senha") ;
    var  strCPF = document.getElementById("cpf").value ; 
 
 
    if(password.value != confirm_password.value) {
     alert("Confira os Campos de Senha Novamente!");
 
     document.formulario.senha.focus() ; 
     return false ;
   } 
 
     if (password == "" || password.value == false || password.value == null ) {
         alert("Não é Permitido Senha Nula")
 
         return false ;
     }
 
 
/*  VALIDA LOGIN */ 
   if (document.getElementById("login").value == "" ) {
      alert("Por Favor ! Preencha o Login") ; 
     return false ; 
   }; 
 
 
 
         /* VALIDA NOME */
 
   if (document.getElementById("nome").value == ""){
      alert("Por Favor ! Preencha o Nome ") ; 
      return false ; 
   } ; 
 
 
 
 
           /* VALIDA EMAIL */
   if (document.getElementById("email_usuario").value == ""){
       alert("Por Favor ! Preencha o Email ") ; 
       return false ; 
   } ; 
 
 
         /*data de nascimento */
   if (document.getElementById("data_nas").value == ""){
     alert("Por Favor ! Preencha a Data de Nascimento ") ; 
     return false ; 
 } ; 
 
 
 
 /*Validação CPF */
 var Soma;
 var Resto;
 Soma = 0 ;
  
 if (strCPF == "00000000000") {
     alert("CPF Inválido") ; 
     return false;
 }
 
 for (i=1; i<=9; i++) {
 Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
 Resto = (Soma * 10) % 11;
 }
 
 if ((Resto == 10) || (Resto == 11)) {
     Resto = 0;
 }
 
 if (Resto != parseInt(strCPF.substring(9, 10)) ) {
     alert("CPF Inválido") ; 
     return false;
 }
 Soma = 0;
 
 for (i = 1; i <= 10; i++) {
      Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);   
 }
 
 Resto = (Soma * 10) % 11;
 
 
 if ((Resto == 10) || (Resto == 11)) {
   Resto = 0;
 }
 
 
 if (Resto != parseInt(strCPF.substring(10, 11) ) )  {
     alert("CPF Inválido ")
     return false;
 }
 return true;
 
 }