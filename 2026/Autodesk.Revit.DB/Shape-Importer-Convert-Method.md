# Shape Importer Convert Method

Source: https://www.revitapidocs.com/2026/be3a172d-dc86-2a49-50ec-fd88d250de87.htm

---

| Shape Importer Convert Method |
| --- |

Converts the geometry stored in the external format into a collection of Revit geometry objects. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<GeometryObject> Convert(
	Document document,
	string filename
)
```

```
Public Function Convert ( 
	document As Document,
	filename As String
) As IList(Of GeometryObject)
```

```
public:
IList<GeometryObject^>^ Convert(
	Document^ document, 
	String^ filename
)
```

```
member Convert : 
        document : Document * 
        filename : string -> IList<GeometryObject> 
```

#### Parameters

document [Document](Document-Class.md)
:   The Revit document where the resulting Revit geometry objects will be used. This document may need to be modified
 to store dependent elements such as graphics styles and/or materials.

filename String
:   The full path to the input file.

#### Return Value

IList [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm) 
A collection of Revit geometry objects created from the incoming data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given filename does not exist. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Data conversion service is not available, or the Material Library is missing. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ShapeImporter Class](Shape-Importer-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
