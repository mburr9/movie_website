import fresh_tomatoes
import media

ghostbusters = media.Movie("Ghostbusters",
                            "Three former parapsychology professors set up shop as a unique ghost removal service.",
                            "https://m.media-amazon.com/images/M/MV5BMTkxMjYyNzgwMl5BMl5BanBnXkFtZTgwMTE3MjYyMTE@._V1_SY1000_CR0,0,650,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=uFWzr2VTCi0")
ghostbustersii = media.Movie("Ghostbusters II",
                            "The discovery of a massive river of ectoplasm and a resurgence of spectral activity allows the staff of Ghostbusters to revive the business.",
                            "https://m.media-amazon.com/images/M/MV5BMTQ2NTk4MjE5Ml5BMl5BanBnXkFtZTgwODIwNjYxMTE@._V1_.jpg",
                            "https://www.youtube.com/watch?v=2yJFCSiyTT4")
beetlejuice = media.Movie("Beetlejuice",
                            "When a recently-deceased ghost couple find their now-vacant home invaded by an obnoxious family, they hire a sleazy ghost who gets rid of humans to help them",
                            "https://m.media-amazon.com/images/M/MV5BZDdmNjBlYTctNWU0MC00ODQxLWEzNDQtZGY1NmRhYjNmNDczXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX670_AL_.jpg",
                            "https://www.youtube.com/watch?v=GuyNP-XyFHs")
zombieland = media.Movie("Zombieland",
                            "A shy student trying to reach his family in Ohio, a gun-toting tough guy trying to find the last Twinkie, and a pair of sisters trying to get to an amusement park join forces to travel across a zombie-filled America.",
                            "https://m.media-amazon.com/images/M/MV5BMTU5MDg0NTQ1N15BMl5BanBnXkFtZTcwMjA4Mjg3Mg@@._V1_SY1000_CR0,0,717,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=8m9EVP8X7N8")
hot_fuzz = media.Movie("Hot Fuzz",
                        "A skilled London police officer is transferred to a small town that's harbouring a dark secret.",
                        "https://m.media-amazon.com/images/M/MV5BMzg4MDJhMDMtYmJiMS00ZDZmLThmZWUtYTMwZDM1YTc5MWE2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,672,999_AL_.jpg",
                        "https://www.youtube.com/watch?v=KOddZELDPmk")
scott_pilgrim = media.Movie("Scott Pilgrim vs. The World",
                        "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
                        "https://m.media-amazon.com/images/M/MV5BMTkwNTczNTMyOF5BMl5BanBnXkFtZTcwNzUxOTUyMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=7wd5KEaOtm4")
movies = [scott_pilgrim, ghostbusters, ghostbustersii, beetlejuice, zombieland, hot_fuzz]
fresh_tomatoes.open_movies_page(movies)
