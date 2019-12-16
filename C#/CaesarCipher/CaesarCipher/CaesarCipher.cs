using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CaesarCipher
{
    class CaesarCipher
    {
        const int OFFSET = 5;
        public static string Encrypt(string plainText)
        {
            string encryptedMsg = "";
            int[] cipherText = new int[plainText.Length];
            char[] chars = plainText.ToCharArray();
            for (var i = 0; i < plainText.Length; i++)
            {
                cipherText[i] = char.IsWhiteSpace(chars[i]) ? chars[i] : chars[i] + OFFSET;
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
                plainText[i] = char.IsWhiteSpace(chars[i]) ? chars[i] : chars[i] - OFFSET;
                decryptedMsg += (char)plainText[i];
            }
            return decryptedMsg;
        }
    }
}
