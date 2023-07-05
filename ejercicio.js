arr=[2,4,1,5,6,3]
let valoresMax=[]
function ValorSuma(arr){
    for(let i=0;i<arr.lenght-1;i++){
        let suma=arr[i]+arr[i+1]
        valoresMax.push(suma)
        }
    return Math.max(...valoresMax)
    }
console.log(ValorSuma(arr))