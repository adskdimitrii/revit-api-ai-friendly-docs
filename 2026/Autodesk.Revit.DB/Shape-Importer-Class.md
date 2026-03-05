# Shape Importer Class

Source: https://www.revitapidocs.com/2026/d6120e08-f260-577d-b6cf-3fe5b042a54e.htm

---

| Shape Importer Class |
| --- |

A utility class that supports conversion of geometry stored in an external format into a Revit geometry objects. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB ShapeImporter 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ShapeImporter : IDisposable
```

```
Public Class ShapeImporter
	Implements IDisposable
```

```
public ref class ShapeImporter : IDisposable
```

```
type ShapeImporter = 
    class
        interface IDisposable
    end
```
The ShapeImporter type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ShapeImporter](4ee1ec99-2ebf-0758-8ffe-d2543012d34b.htm) | Default constructor. Initializes an instance of ShapeImporter that will automatically recognize the file format from its extension (ShapeImporterSourceFormat.Auto). |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DefaultLengthUnit](eb2463a0-6dd7-5f34-c0ae-7125776b973f.htm) | The length unit to be used if not specified when the input is a unitless SAT file. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [InputFormat](ff8a86a4-620e-1077-426b-540bd27027e6.htm) | The format of the incoming data. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](d48b1ede-f225-e449-70bb-67145f62caf4.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Convert](Shape-Importer-Convert-Method.md) | Converts the geometry stored in the external format into a collection of Revit geometry objects. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](710c3d7a-957f-dbc0-50c0-39cc83bbf92c.htm) | Releases all resources used by the ShapeImporter |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsServiceAvailable](Shape-Importer-Is-Service-Available-Method.md) | Checks whether the data conversion service and Material Library are available. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetDefaultLengthUnit](41ffab1e-4b54-72e0-7eb4-ad44dee582bc.htm) | Sets the length unit to be used when the input is a unitless SAT file. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks See [ShapeImporterSourceFormat](Shape-Importer-Source-Format-Enumeration.md) for the list of supported formats. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
