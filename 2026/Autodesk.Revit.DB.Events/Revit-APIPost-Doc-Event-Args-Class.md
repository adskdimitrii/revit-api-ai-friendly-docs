# Revit APIPost Doc Event Args Class

Source: https://www.revitapidocs.com/2026/7d3fba7a-5efb-6a4c-a49c-16c25f972830.htm

---

| Revit APIPost Doc Event Args Class |
| --- |

The base class used for post events where the arguments must supply access to the document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
System EventArgs 
[Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) 
[Autodesk.Revit.DB.Events RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm) 
Autodesk.Revit.DB.Events RevitAPIPostDocEventArgs 
[More](#fullInheritance) 
**Namespace:** [Autodesk.Revit.DB.Events](../ungrouped/Autodesk.-Revit.-DB.-Events-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RevitAPIPostDocEventArgs : RevitAPIPostEventArgs
```

```
Public Class RevitAPIPostDocEventArgs
	Inherits RevitAPIPostEventArgs
```

```
public ref class RevitAPIPostDocEventArgs : public RevitAPIPostEventArgs
```

```
type RevitAPIPostDocEventArgs = 
    class
        inherit RevitAPIPostEventArgs
    end
```
The RevitAPIPostDocEventArgs type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.htm) | Indicates whether an event may be cancelled by an event delegate. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Document](b0a5235e-b2b3-0a29-799c-2ef535a51909.htm) | The document associated with the event. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Status](01c1c4b6-fc91-0651-3312-4d988073433a.htm) | Indicates whether the action associated with this event succeeded, failed, or was cancelled (by an API event handler). (Inherited from [RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
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
[Autodesk.Revit.DB.Events RevitAPIPostEventArgs](93554f52-0145-3454-5697-3f1015e46434.htm) 
Autodesk.Revit.DB.Events RevitAPIPostDocEventArgs 
[Autodesk.Revit.DB.Events DocumentCreatedEventArgs](bd300a6c-382a-60f0-a8b4-eae4a8368bf9.htm) 
[Autodesk.Revit.DB.Events DocumentOpenedEventArgs](0c6c3227-ecad-6a5f-c1b1-d08745360637.htm) 
[Autodesk.Revit.DB.Events DocumentPrintedEventArgs](12e3944c-0c43-8c08-d3d0-15828d9a6337.htm) 
[Autodesk.Revit.DB.Events DocumentReloadedLatestEventArgs](0e00db2f-a160-8922-e993-346a9040bc5d.htm) 
[Autodesk.Revit.DB.Events DocumentSavedAsEventArgs](6ac311cc-14e9-639f-a8d7-e321927e0c14.htm) 
[Autodesk.Revit.DB.Events DocumentSavedEventArgs](7bcc6ea7-4e7e-588b-232d-ed94d70d2c5e.htm) 
[Autodesk.Revit.DB.Events DocumentSynchronizedWithCentralEventArgs](ff0bae6e-c1b8-7b7a-cbc9-3b419b7b0c48.htm) 
[Autodesk.Revit.DB.Events ElementTypeDuplicatedEventArgs](7ec2ef50-ea02-2e47-a854-490d00285cd1.htm) 
[Autodesk.Revit.DB.Events FamilyLoadedIntoDocumentEventArgs](a63d4c02-fc75-445b-edf5-d9068465fb1a.htm) 
[Autodesk.Revit.DB.Events FileExportedEventArgs](8f668506-1f9b-0282-f6df-66428891ad3b.htm) 
[Autodesk.Revit.DB.Events FileImportedEventArgs](87f5b053-2c42-7b57-a58d-4b2489f461cc.htm) 
[Autodesk.Revit.DB.Events LinkedResourceOpenedEventArgs](4d82ed63-8fd2-71a9-52e8-4695ab299b1b.htm) 
[Autodesk.Revit.DB.Events ViewExportedEventArgs](d0e95c70-c5f4-8b12-2f7a-5279ba667948.htm) 
[Autodesk.Revit.DB.Events ViewPrintedEventArgs](8d683cd4-c19b-034f-8b42-653b024e7aa4.htm) 
[Autodesk.Revit.DB.Events ViewsExportedByContextEventArgs](141e1a8c-7675-bb1f-fe54-eaf00b2bd75b.htm) 
[Autodesk.Revit.UI.Events ViewActivatedEventArgs](3c54cedc-bdbd-fb2c-2250-cb7387a5c3d4.htm)
