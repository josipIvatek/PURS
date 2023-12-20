SELECT * FROM temperatura;

SELECT * FROM temperatura ORDER BY id DESC LIMIT 1;

SELECT ime, prezime, naziv FROM korisnik
LEFT JOIN ovlasti ON korisnik.id_ovlasti=ovlasti.id;

SELECT * FROM korisnik WHERE username = 'kkolar' AND password = '12ab';

SELECT ime, prezime, vrijednost FROM korisnik
LEFT JOIN temperatura ON korisnikove_temperature.id_temperature=temperatura.id
LEFT JOIN korisnikove_temperature ON korisnik.id=korisnikove_temperature.id_temperature;