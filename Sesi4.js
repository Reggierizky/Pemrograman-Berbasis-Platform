const filmInterstellar = {
    // Properti film
    judul: "Interstellar",
    tahunRilis: 2014,
    sutradara: "Christopher Nolan",
    genre: ["Sci-Fi", "Adventure", "Drama"],

    // Method untuk menampilkan detail
    tampilkanDetail: function() {
        return `
            Detail Film:
            Judul: ${this.judul}
            Tahun Rilis: ${this.tahunRilis}
            Sutradara: ${this.sutradara}
            Genre: ${this.genre.join(", ")}
        `.trim(); // .trim() untuk menghilangkan spasi kosong di awal dan akhir string
    }
};// Akses nilai dari properti sutradara
console.log("Sutradara:", filmInterstellar.sutradara);

// Akses nilai dari elemen kedua dalam properti genre (indeks 1)
console.log("Genre Kedua:", filmInterstellar.genre[1]);

// Akses dan tampilkan hasil pemanggilan method tampilkanDetail
console.log("\n--- Detail Lengkap ---");
console.log(filmInterstellar.tampilkanDetail());