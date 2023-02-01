using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing.Imaging;
using System.Windows.Forms;
using System.Collections;
using System.IO;
namespace IRImageReaderDemo
{
    class Exif
        : System.Windows.Forms.ListView
    {
        public enum PropertyTagType
        {
            Byte = 1,
            ASCII = 2,
            Short = 3,
            Long = 4,
            Rational = 5,
            Undefined = 7,
            SLONG = 9,
            SRational = 10
        }

        string GetStringFromProperty(PropertyTagType type, Byte[] bytes)
        {
            switch (type)
            {
                case PropertyTagType.Byte:
                    {
                        return bytes[0].ToString();
                    }

                case PropertyTagType.ASCII:
                    {
                        StringBuilder sb;

                        sb = new StringBuilder();
                        for (int i = 0; i < bytes.Length; i++)
                        {
                            if (!Char.IsControl((char)bytes[i]))
                            {
                                sb.Append((char)bytes[i]);
                            }
                            else
                            {
                                sb.Append("\\" + bytes[i].ToString());
                            }
                        }
                        return sb.ToString();
                    }

                case PropertyTagType.Short:
                    {
                        ushort s;

                        s = (ushort)(bytes[1] * 256 + bytes[0]);
                        return s.ToString();
                    }

                case PropertyTagType.Long:
                    {
                        uint l;

                        l = (uint)(bytes[3] * 16777216 + bytes[2] * 65536 + bytes[1] * 256 + bytes[0]);
                        return l.ToString();
                    }

                case PropertyTagType.SRational:
                    {
                        ushort numerator;
                        ushort denominator;

                        numerator = (ushort)(bytes[1] * 256 + bytes[0]);
                        denominator = (ushort)(bytes[3] * 256 + bytes[2]);
                        return String.Format("{0} / {1})", numerator, denominator);
                    }


                case PropertyTagType.Rational:
                    {
                        uint numerator;
                        uint denominator;

                        numerator = (uint)(bytes[3] * 16777216 + bytes[2] * 65536 + bytes[1] * 256 + bytes[0]);
                        denominator = (uint)(bytes[7] * 16777216 + bytes[6] * 65536 + bytes[5] * 256 + bytes[4]);
                        return String.Format("{0} / {1}", numerator, denominator);
                    }

                default:
                    {
                        return "<" + type.ToString() + ">";
                    }
            }
        }

        public void RefreshEXIF(string fileName)
        {
            try
            {
                Items.Clear();
                if (Path.GetExtension (fileName) != ".jpg")
                {
                    return;
                }
                // Add new EXIF items
                using(System.Drawing.Image theImage = new System.Drawing.Bitmap(fileName))
				{
	                foreach (int propId in theImage.PropertyIdList)
	                {
	                    PropertyItem item = theImage.GetPropertyItem(propId);
	                    ListViewItem lItem = new ListViewItem(propId.ToString());
	                    lItem.SubItems.Add(GetStringFromProperty((PropertyTagType)item.Type, item.Value));
	                    Items.Add(lItem);
	                }
				}
            }
            catch (Exception ex)
            {
                string message = String.Format("An error occured when trying to iterate through EXIF tags: \n\n{0}", ex.ToString());
                if (ex.Data != null)
                {
                    if (ex.Data.Count > 0)
                        message += ", Extra details: ";
                    foreach (DictionaryEntry de in ex.Data)
                        message += string.Format(" key='{0}' - value='{1}'", de.Key, de.Value);
                }
                if (ex.InnerException != null)
                {
                    if (ex.InnerException.Data.Count > 0)
                        message += ", Extra inner details: ";
                    foreach (DictionaryEntry de in ex.InnerException.Data)
                        message += string.Format(" key='{0}' - value='{1}'", de.Key, de.Value);
                }
            }
        }
    }
}
