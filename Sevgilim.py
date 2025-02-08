<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sevgilim için Web Sitesi</title>
  <style>
    body {
      background-color: #000;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h1, h2 {
      color: #f00;
    }
    .container {
      margin-top: 50px;
    }
    .button {
      background-color: #f00;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Sevgilim, hoş geldin!</h1>
    <p>Bu site seni seviyorum demek için özel olarak hazırlandı.</p>
    <button class="button" onclick="window.location.href='game.html'">Macera Oyununa Başla!</button>
  </div>
  <footer>
    <p>Şarkıyı dinle: <iframe src="https://open.spotify.com/embed/track/5kpkEb0M49YM516trGUSWS?si=b1tXun6iTQm3BYbj2epOOQ" width="300" height="380" frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe></p>
  </footer>
</body>
</html>
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Macera Oyunu</title>
  <style>
    body {
      background-color: #000;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h1 {
      color: #f00;
    }
    .button {
      background-color: #f00;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <h1>Macera Başlıyor!</h1>
  <p>İlk görevini başarıyla tamamladın. Şimdi yeni bir macera seni bekliyor!</p>
  <button class="button" onclick="window.location.href='secret.html'">Sürpriz Bölümüne Git</button>
</body>
</html>
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sürpriz Bölümü</title>
  <style>
    body {
      background-color: #000;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h1 {
      color: #f00;
    }
  </style>
</head>
<body>
  <h1>Şifreyi Gir:</h1>
  <input type="password" id="password" placeholder="Şifreyi girin" />
  <button class="button" onclick="checkPassword()">Gönder</button>
  <p id="message"></p>

  <script>
    function checkPassword() {
      const password = document.getElementById('password').value;
      const message = document.getElementById('message');
      if (password === 'Ne olursa olsun yanındayım') {
        message.innerHTML = 'Tebrikler, sürpriz mesajını açtın!';
      } else {
        message.innerHTML = 'Yanlış şifre! Tekrar deneyin.';
      }
    }
  </script>
</body>
</html>
body {
  background-color: #000;
  color: white;
  font-family: Arial, sans-serif;
  text-align: center;
}
h1, h2 {
  color: #f00;
}
.button {
  background-color: #f00;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 18px;
}