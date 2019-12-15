using System;
using System.Collections.Generic;
using System.IO;

namespace CaesarCipher
{
    class Program
    {
        static void Main(string[] args)
        {
            string continueResp = "yes";
            string filepath = "";
            while(continueResp.Equals("yes", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Select an operation:\n1)Encypt\n2)Decrypt\n3)Quit");
                int op = Convert.ToInt32(Console.ReadLine());

                switch(op)
                {
                    case (int)Operations.Encrypt:

                        Console.WriteLine("Enter the filepath of the file: ");
                        filepath = Console.ReadLine();
                        Console.WriteLine("Encrypting file...");
                        if (File.Exists(filepath))
                        {
                            var msgToEncrypt = File.ReadAllText(filepath);
                            var encryptedMsg = Encrypt(msgToEncrypt);
                            var encryptedFile = filepath.Replace(".txt", "Encrypted.txt");
                            File.WriteAllText(encryptedFile, encryptedMsg);
                            Console.WriteLine(encryptedMsg);
                        }
                        else
                        {
                            Console.WriteLine("File does not exist. Try again");
                        }
                        break;
                    case (int)Operations.Decrypt:

                        Console.WriteLine("Enter the filepath of the file: ");
                        filepath = Console.ReadLine();
                        Console.WriteLine("Decrypting file...");
                        //open file
                        if (File.Exists(filepath))
                        {
                            var msgToDecrypt = File.ReadAllText(filepath);
                            var decryptedMsg = Decrypt(msgToDecrypt);
                            var decryptedFile = filepath.Replace(".txt", "Decrypted.txt");
                            File.WriteAllText(decryptedFile, decryptedMsg);
                            Console.WriteLine(decryptedMsg);
                        }
                        else
                        {
                            Console.WriteLine("File does not exist. Try again");
                        }
                        break;
                    case (int)Operations.Quit:
                        Environment.Exit(1);
                        break;
                    default:
                        Console.WriteLine("Invalid operation. Try again.\n");
                        continue;
                }

                Console.WriteLine("Continue operations (yes/no)?");
                continueResp = Console.ReadLine();
            }
        }

        public static string Encrypt(string plainText)
        {
            string encryptedMsg = "";
            int[] cipherText = new int[plainText.Length];
            char[] chars = plainText.ToCharArray();
            for(var i = 0; i < plainText.Length; i++)
            {
                cipherText[i] =  chars[i] + 5;
                encryptedMsg += (char)cipherText[i];
            }
            return encryptedMsg;
        }

        public static string Decrypt(string cipherText)
        {
            string decryptedMsg = "";
            int[] plainText = new int[cipherText.Length];
            char[] chars = cipherText.ToCharArray();
            for (var i = 0; i < plainText.Length; i++)
            {
                plainText[i] = chars[i] - 5;
                decryptedMsg += (char)plainText[i];
            }
            return decryptedMsg;
        }
        enum Operations
        {
            Encrypt = 1, Decrypt, Quit
        };
    }
}
