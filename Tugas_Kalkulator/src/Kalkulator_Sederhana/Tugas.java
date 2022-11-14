package Kalkulator_Sederhana;

import java.util.Scanner;

public class Tugas {

    public static void main(String[] args) {
//      deklarasi variabel
        String pilih_operasi;
        int nilai_a = 0;
        int nilai_b = 0;
        double hasil;

        Scanner input_pilihan = new Scanner(System.in);
        System.out.println("__________________________");
        System.out.println("PILIHLAH OPERASI ARITMATIKA: ");
        System.out.println("----------------------------");
        System.out.println("1.Penjjumlahan");
        System.out.println("2.Penguragan");
        System.out.println("3.Perkalian");
        System.out.println("4.Pembagian");
        System.out.println("5. Perpangkatan");
        System.out.println("________________________________");
        System.out.println("masukkan Pilihan (1/2/3/4/5) : ");
        pilih_operasi = input_pilihan.nextLine();

//       logika 
        if (pilih_operasi.equals("1")) {
            System.out.print("Masukkan nilai A : ");
            nilai_a = input_pilihan.nextInt();
            System.out.print("Masukkan nilai B : ");
            nilai_b = input_pilihan.nextInt();
//operasi penjumlahan
            hasil = nilai_a + nilai_b;
            System.out.println("Hasil Penjumlahan adalah : " + hasil);

        } else if (pilih_operasi.equals("2")) {
            System.out.print("Masukkan nilai A : ");
            nilai_a = input_pilihan.nextInt();
            System.out.print("Masukkan nilai B : ");
            nilai_b = input_pilihan.nextInt();
//operasi pengurangan
            hasil = nilai_a - nilai_b;
            System.out.println("Hasil Pengurangan adalah : " + hasil);

        } else if (pilih_operasi.equals("3")) {
            System.out.print("Masukkan nilai A : ");
            nilai_a = input_pilihan.nextInt();
            System.out.print("Masukkan nilai B : ");
            nilai_b = input_pilihan.nextInt();
//            operasi perkalian
            hasil = nilai_a * nilai_b;
            System.out.println("Hasil Perkalian adalah : " + hasil);

        } else if (pilih_operasi.equals("4")) {
            System.out.print("Masukkan nilai A : ");
            nilai_a = input_pilihan.nextInt();
            System.out.print("Masukkan nilai B : ");
            nilai_b = input_pilihan.nextInt();
//oprasi pembagian
            hasil = nilai_a / nilai_b;
            System.out.println("Hasil Pembagian adalah : " + hasil);

        } else if (pilih_operasi.equals("5")) {
            System.out.print("Masukkan nilai A : ");
            nilai_a = input_pilihan.nextInt();
            System.out.print("Masukkan nilai B : ");
            nilai_b = input_pilihan.nextInt();
//opersi perpangkatan 
//menggunakan fungsi Math.pow di gunakan utuk perpangkatan bilangan
            hasil = Math.pow(nilai_a, nilai_b);
            System.out.println("Hasil perpangkatan adalah : " + hasil);
        } else {
            System.out.println("Pilihan tidak ada!");
        }

    }
}
