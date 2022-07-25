$(()=>{
  billsTotal = parseInt($("#bills-total").html())
  bank = parseInt($("#ammount-in-bank").html())
  balance = bank - billsTotal
  $("#balance").html(balance)
  
})
