# Importer IFC Class

Source: https://www.revitapidocs.com/2026/87327a4b-94fd-5a21-df33-9beb1921cb4d.htm

---

| Importer IFC Class |
| --- |

The main class provided by Revit to allow implementation of IFC import. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.IFC ImporterIFC 
  
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ImporterIFC : IDisposable
```

```
Public Class ImporterIFC
	Implements IDisposable
```

```
public ref class ImporterIFC : IDisposable
```

```
type ImporterIFC = 
    class
        interface IDisposable
    end
```
The ImporterIFC type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](5b2ccc42-7130-5d2c-38e8-b6e84a290b35.htm) | Gets the document associated with the import. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [FullFileName](ad440967-6daf-bb3e-6066-9ceccee0bab3.htm) | The full file name of the IFC file to be import. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](3520bb7b-fd72-99d9-358a-79fd63ab80e9.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](590b60e1-fe30-0664-3efb-f204708c8821.htm) | Releases all resources used by the ImporterIFC |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetOptions](86a8602c-c23f-0170-33b6-04a6e53a8d54.htm) | Gets the collection of named options set by the importer client. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ProcessIFCProject(IFCAnyHandle)](5c81eabb-0622-f97b-fe4c-8fae55f6ff68.htm) | The entry point to the native IFC import function. Processes the main IfcProject and creates appropriate Revit elements. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ProcessIFCProject(IFCAnyHandle, IDictionary IFCAnyHandle, ElementId )](bf0ee7d6-d33b-d6a6-993d-f69d3dc583a6.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetFile](4b33d4c1-a06b-400d-7ecc-d3b24b3413aa.htm) | Sets the handle to the IFC file being created during this import operation. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks An instance of this class is provided to clients which implement IImporterIFC
 in order to provide an implementation for IFC import. It contains information
 on the options selected by the user for the import operation, as well as
 members used to access specific types of data needed to implement the import
 properly. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
