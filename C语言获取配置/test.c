#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define _LINE_SIZE_ 256
#define _FLAG_INIT_VALUE _LINE_SIZE_+1
#define _KEY_SIZE_ 256
#define _VALUE_SIZE_ 256
#define _CONFIG_SIZE_ 16

typedef struct KV{
    char key[_KEY_SIZE_];
    char value[_VALUE_SIZE_];
}KV;

typedef struct Config{
    KV *pair;
    int size;
    int used;
}Config;

//扩容
void resizeConfigSize(Config *config){
    int oldsize = config->size;
    config->size = config->size<<1;
    KV *newpair = (KV*)malloc(sizeof(KV)*config->size);
    memmove(newpair,config->pair,oldsize*sizeof(KV));
    config->pair = newpair;
}
void get_key_value(char *line,char *key,char *value){
    int flag=_FLAG_INIT_VALUE;//用于记录等于号位置和分割标记
    for(int i=0;i<strlen(line);i++){
        if(line[i]=='='){
            if(i<flag)//记录第一次出现的等于号
                flag=i;
            key[i]='\0';
        }
        if(flag==_FLAG_INIT_VALUE)//key
            key[i] = line[i];
        else{//value
            value[i-flag-1] = line[i];
        }
    }
    //printf("%s=%s\n",key,value);
}
//初始化配置结构体
Config loadConfig(char *filename){
    FILE *file = fopen(filename,"r");
    int currentindex=0;
    Config config;
    config.size = _CONFIG_SIZE_;
    config.pair = (KV *)malloc(sizeof(KV)*_CONFIG_SIZE_);
    config.used = 0;

    while(!feof(file)){
        char line[_LINE_SIZE_];
        if(fgets(line,_LINE_SIZE_,file)==NULL){
            printf("read error\n");
            break;
        }
        if(currentindex>=config.size)//扩容
            resizeConfigSize(&config);
        get_key_value(line,config.pair[currentindex].key,config.pair[currentindex].value);
        //printf("##%s\n",config.pair[currentindex].key);
        currentindex++;
    }
    config.used = currentindex;
    return config;
}

int main()
{
    // FILE * file = fopen("./config","r");
    // while(!feof(file)){
    //     char line[_LINE_SIZE_];
    //     int flag=_FLAG_INIT_VALUE;//用于记录等于号位置和分割标记
    //     char key[_LINE_SIZE_]={0},value[_LINE_SIZE_]={0};
    //     if(fgets(line,_LINE_SIZE_,file)==NULL){
    //         printf("read error\n");
    //         break;
    //     }
    //     for(int i=0;i<strlen(line);i++){
    //         if(line[i]=='='){
    //             if(i<flag)//记录第一次出现的等于号
    //                 flag=i;
    //             key[i]='\0';
    //         }
    //         if(flag==_FLAG_INIT_VALUE)//key
    //             key[i] = line[i];
    //         else{//value
    //             value[i-flag-1] = line[i];
    //         }
    //     }
    //     printf("%s=%s\n",key,value);
    // }
    Config config = loadConfig("./config");
    for(int i=0;i<config.used;i++)
        printf("%s=%s\n",config.pair[i].key,config.pair[i].value);
    return 0;
}