import datetime
import os
import fitz  # fitz就是pip install PyMuPDF

def pyMuPDF_fitz(pdfPath, imagePath, amplification):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.page_count):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = amplification
        zoom_y = amplification
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.save(imagePath + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('处理完成！\n处理时间 =', (endTime_pdf2img - startTime_pdf2img).seconds,'s')

if __name__ == "__main__":
    # 1、PDF地址
    pdfPath = input("PDF地址:")
    # 2、需要储存图片的目录
    imagePath = input("IMG地址:")
    # 3、放大倍数
    # 默认图片大小为：792X612, dpi=96 (1.33333333-->1056x816)   (2-->1584x1224)
    print("默认图片大小为：792X612, dpi=96 (1.33333333-->1056x816)   (2-->1584x1224)")
    amplification = input("图片质量（1.3-2）:")
    pyMuPDF_fitz(pdfPath, imagePath, amplification)