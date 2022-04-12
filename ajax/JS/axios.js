var currenttime = new Date()
// currenttime.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
// var moment = require('moment')

axios({
    method: 'get',
    url: 'https://api.unsplash.com/photos/random?client_id=kJF3qw553xaWBR5Mhwxqk4oO6A7sg0bDgiHUy685MOM'
  })

//   response is a placeholder
.then((response) =>{
    console.log(response)
    // $('body').append(`<img src=${response.data.urls.raw}</img>`)
    $("body").css("background-image", "url(" + response.data.urls.regular + ")");
    $("body").css({
        "height": "auto",
        "width": "100%",
    })
    // $("body").append(`<title>${moment().format('LTS') }</title>`)
})
.catch((error) => {
    console.log("your mom")
})


$(document).ready(function(){    
if (currenttime.getHours() >=12 && currenttime.getHours() <17){
    $("body").append(`<h3>${currenttime.getHours()}:${currenttime.getMinutes()}</h3><h4>Good Afternoon, Lila</h4>`);
} else if (currenttime.getHours() >=17 && currenttime.getHours() <20){
    $("body").append(`<h3>${currenttime.getHours()}:${currenttime.getMinutes()}<h3><h4>Good Evening, Lila</h4>`);
}else if ((currenttime.getHours() >= 1 && currenttime.getHours() <12 )|| currenttime.getHours()==24){
    $("body").append(`<h3>${currenttime.getHours()}:${currenttime.getMinutes()}<h3><h4>Good Morning Lila!</h4>`);
}
else if (currenttime.getHours() >= 20 && currenttime.getHours() <24){
    $("body").append(`<h3>${currenttime.getHours()}:${currenttime.getMinutes()}</h3><h4>Good Night, Lila</h4>`);
}})


axios({
    method: 'get',
    url: "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
  })
.then((response) =>{
    console.log(response.data.quoteText, response.data.quoteAuthor)
    $("body").append(`<h3>${currenttime.getHours()}:${currenttime.getMinutes()}</h3>`)
    $('body').append(`<h1 class="bottom-center">${response.data.quoteText} - ${response.data.quoteAuthor}</h1>`)
    // $("h1").css({"position": "absolute", "bottom": "0", "width": "100%","height": "2.5rem"})

})

.catch((error) => {
    console.log("your mom")
})


axios({
    method: 'get',
    url: "https://api.openweathermap.org/data/2.5/weather?q=Toronto&appid=90207e2df89e95452154840f30f8163b&units=metric"
  })
.then((response) =>{
    const icons = {
        clear: '☀',
        rain: '️🌧',
        storm: '⛈',
        snow: '🌨',
        mist: '🌫',
        clouds: '☁',
      };
    
    roundedTemp = Math.round(response.data.main.temp,1)
    cityname= response.data.name
    console.log(response.data.weather[0].main.toLowerCase())
    $('body').append(`<h2 class="temp">${icons[response.data.weather[0].main.toLowerCase()]} ${roundedTemp}°C </h2>`)
})
.catch((error) => {
    console.log("your mom")
})



// background image fetchd from API as background image
// temp fetched from API, and display it top right hand corner
// quotation, middle at the bottom
// current time -> good morning, afternoon, night