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
            string filepath;
            while(continueResp.Equals("yes", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Select an operation:\n1)Encypt\n2)Decrypt\n3)Quit");
                int op = Convert.ToInt32(Console.ReadLine());

                switch(op)
                {
                    case (int)Operations.Encrypt:

                        Console.WriteLine("Enter the filepath of the file: ");
                        filepath = Console.ReadLine();
                        try
                        {
                            if (File.Exists(filepath))
                            {
                                Console.WriteLine("Encrypting file...");
                                var msgToEncrypt = File.ReadAllText(filepath);
                                var encryptedMsg = CaesarCipher.Encrypt(msgToEncrypt);
                                var encryptedFile = filepath.Replace(".txt", "Encrypted.txt");
                                File.WriteAllText(encryptedFile, encryptedMsg);
                                Console.WriteLine(encryptedMsg);
                            }
                            else
                            {
                                Console.WriteLine("File does not exist. Try again");
                            }
                        }
                        catch(Exception e)
                        {
                            Console.WriteLine(e.Message);
                            continue;
                        }
                        break;
                    case (int)Operations.Decrypt:

                        Console.WriteLine("Enter the filepath of the file: ");
                        filepath = Console.ReadLine();
                        try
                        {
                            if (File.Exists(filepath))
                            {
                                Console.WriteLine("Decrypting file...");
                                var msgToDecrypt = File.ReadAllText(filepath);
                                var decryptedMsg = CaesarCipher.Decrypt(msgToDecrypt);
                                var decryptedFile = filepath.Replace(".txt", "Decrypted.txt");
                                File.WriteAllText(decryptedFile, decryptedMsg);
                                Console.WriteLine(decryptedMsg);
                            }
                            else
                            {
                                Console.WriteLine("File does not exist. Try again");
                            }
                        }
                        catch (Exception e)
                        {
                            Console.WriteLine(e.Message);
                            continue;
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

        enum Operations
        {
            Encrypt = 1, Decrypt, Quit
        }
    }
}
