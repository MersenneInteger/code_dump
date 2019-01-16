//jewels and stones

int numJewelsInStones(char* J, char* S) {
    
    int common = 0;

    for(int i = 0; i < strlen(J); i++) {
        for(int k = 0; k < strlen(S); k++){
            if (S[k] == J[i])
                common++;
        }
    }
    return common;
}

int main(int argc, char** argv)
{
    print(numJewelsInStones('aA','aAAbbb'));
}