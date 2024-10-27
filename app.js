const http = require('http');
const express = require('express');
const socketIO = require('socket.io');
const path = require('path');
const app = express();
const server = http.createServer(app);
const io = socketIO(server);
const ejs = require('ejs')
app.use(express.static('public'));

app.set('view engine', 'ejs')
app.get("/", (req, res) => {
 res.render('home')

});
io.on('connection', (socket) => {

  console.log('Client connected');
  socket.on('mag', (data) => {
    console.log('Received mag data:', data);
    socket.broadcast.emit('mag', data);
  });
  socket.on('adxl', (data) => {
    console.log('Received adxl data:', data);
    socket.broadcast.emit('adxl', data);
  });



  socket.on('vth', (data) => {
    console.log('Received vth data:', data);
    socket.broadcast.emit('vth', data);
  });



  socket.on('co', (data) => {
    console.log('Received co data:', data);
    socket.broadcast.emit('co', data);
  });

  socket.on('gps', (data) => {
    console.log('Received gps data:', data);
    socket.broadcast.emit('gps', data);
  });

  socket.on('bmp', (data) => {
    console.log('Received bmp data:', data);
    socket.broadcast.emit('bmp', data);
  });
  socket.on('responsemsg', (data)=>{
    socket.broadcast.emit("responsemsg",data)
  })
  socket.on('chatMessage',(data)=>{
    console.log(data)
    socket.broadcast.emit("chatMessage",data)
  })




  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

const PORT = 3000;
server.listen(PORT, (req,res) => {
  console.log(`Server running on http://127.0.0.1:3000`);
});
