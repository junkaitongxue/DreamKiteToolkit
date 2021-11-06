import hashlib
import base64


class Encrypts:
    """加密方法: MD5 base64"""

    @staticmethod
    def md5_encrypt(plaintext):
        """ MD5加密
        :param plaintext: 需要加密的内容
        :return: encrypt_str密文
        """
        h1 = hashlib.md5()  # 创建md5对象
        h1.update(plaintext.encode(encoding='utf-8'))  # 必须声明encode
        # 加密
        encrypt_str = h1.hexdigest()
        return encrypt_str

    @staticmethod
    def base64_encry(plaintext):
        """base64加密"""
        base64_encry = base64.b64encode(plaintext.encode('utf-8'))
        return base64_encry


class Decrypts:
    """base64"""
    @staticmethod
    def base64_decry(ciphertext):
        """base64解密"""
        base64_decry = (base64.b64decode(ciphertext)).decode('utf-8')
        return base64_decry


if __name__ == '__main__':
    print(Encrypts.md5_encrypt('hello') == "5d41402abc4b2a76b9719d911017c592")
    print(Decrypts.base64_decry(Encrypts.base64_encry('hello')))
