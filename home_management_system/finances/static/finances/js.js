$(()=>{
  console.log("jquery");

  $(".add-new-bill-button-class").click((e)=>{
    console.log($(".add-new-bill-button-class").parent());
  })



  $(".paycheck-table").click((e)=>{
    console.log($(".paycheck-table").parent());
  })
})
