# Revit APIPre Doc Event Args Class

Source: https://www.revitapidocs.com/2026/ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.htm

---

| Revit APIPre Doc Event Args Class |
| --- |

The base class used for pre events where the arguments must supply access to the document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
System EventArgs 
[Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) 
[Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm) 
Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs 
[More](#fullInheritance) 
**Namespace:** [Autodesk.Revit.DB.Events](../ungrouped/Autodesk.-Revit.-DB.-Events-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RevitAPIPreDocEventArgs : RevitAPIPreEventArgs
```

```
Public Class RevitAPIPreDocEventArgs
	Inherits RevitAPIPreEventArgs
```

```
public ref class RevitAPIPreDocEventArgs : public RevitAPIPreEventArgs
```

```
type RevitAPIPreDocEventArgs = 
    class
        inherit RevitAPIPreEventArgs
    end
```
The RevitAPIPreDocEventArgs type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.htm) | Indicates whether an event may be cancelled by an event delegate. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](ccbc5e47-3964-cf1e-4cac-fa023d3b8e63.htm) | The document associated with the event. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Cancel](88fa78de-0fff-a85f-0de3-b631673e9e51.htm) | When the event is cancellable, may call the Cancel() method to cancel it. (Inherited from [RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](697794d0-db4b-41ee-90a3-388296ffeefb.htm) | (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCancelled](5627aeaa-9d9c-dcbe-b34f-db40f1c025be.htm) | Indicates whether the event is being cancelled. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Events Namespace](../ungrouped/Autodesk.-Revit.-DB.-Events-Namespace.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
System EventArgs 
[Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) 
[Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm) 
Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs 
[Autodesk.Revit.DB.Events DocumentClosingEventArgs](939d187e-051c-6a8a-0bb9-6c030b0911a4.htm) 
[Autodesk.Revit.DB.Events DocumentPrintingEventArgs](cae91da6-7e05-e47c-5957-15330428c303.htm) 
[Autodesk.Revit.DB.Events DocumentReloadingLatestEventArgs](0952bb8e-fa8d-382a-ba2b-97bbbc820a99.htm) 
[Autodesk.Revit.DB.Events DocumentSavingAsEventArgs](1bb9bb9f-be64-3c6f-804b-66fe6a2b0562.htm) 
[Autodesk.Revit.DB.Events DocumentSavingEventArgs](e812523c-81f5-454f-9868-4332ab6c74a9.htm) 
[Autodesk.Revit.DB.Events DocumentSynchronizingWithCentralEventArgs](d6859206-10ee-9570-a1a8-98a68f3e1fd9.htm) 
[Autodesk.Revit.DB.Events ElementTypeDuplicatingEventArgs](a507c83d-21c0-badf-ee5d-f5e4c76886a8.htm) 
[Autodesk.Revit.DB.Events FamilyLoadingIntoDocumentEventArgs](e2dcca36-38d1-8bc9-d9f5-fd52bbd5ba0f.htm) 
[Autodesk.Revit.DB.Events FileExportingEventArgs](33fecf48-ec69-4d54-8e73-4f8b6233a744.htm) 
[Autodesk.Revit.DB.Events FileImportingEventArgs](be397e59-7332-cb8f-426d-ebe7f420e0c9.htm) 
[Autodesk.Revit.DB.Events ViewExportingEventArgs](46171adf-d115-9796-b6f7-7d1e27d5d3b5.htm) 
[Autodesk.Revit.DB.Events ViewPrintingEventArgs](8e7d048f-a50b-7903-6001-6716f7eabdb5.htm) 
[Autodesk.Revit.DB.Events ViewsExportingByContextEventArgs](5db665aa-f9cb-f204-72e0-eff6597a9a9d.htm) 
[Autodesk.Revit.UI.Events TransferringProjectStandardsEventArgs](ffc4e960-25e8-9edb-f660-d328c57e65d0.htm) 
[Autodesk.Revit.UI.Events ViewActivatingEventArgs](3b279e84-422c-ddc4-44df-fa5498124b14.htm)
