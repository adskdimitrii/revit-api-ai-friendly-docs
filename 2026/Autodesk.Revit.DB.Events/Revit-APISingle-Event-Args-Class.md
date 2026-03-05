# Revit APISingle Event Args Class

Source: https://www.revitapidocs.com/2026/446fa3c6-4f35-47f4-e8c2-e5235c321836.htm

---

| Revit APISingle Event Args Class |
| --- |

The class is used as a base class for arguments of any single\-event. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
System EventArgs 
[Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) 
Autodesk.Revit.DB.Events RevitAPISingleEventArgs 
[More](#fullInheritance) 
**Namespace:** [Autodesk.Revit.DB.Events](../ungrouped/Autodesk.-Revit.-DB.-Events-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class RevitAPISingleEventArgs : RevitAPIEventArgs
```

```
Public Class RevitAPISingleEventArgs
	Inherits RevitAPIEventArgs
```

```
public ref class RevitAPISingleEventArgs : public RevitAPIEventArgs
```

```
type RevitAPISingleEventArgs = 
    class
        inherit RevitAPIEventArgs
    end
```
The RevitAPISingleEventArgs type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.htm) | Indicates whether an event may be cancelled by an event delegate. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](697794d0-db4b-41ee-90a3-388296ffeefb.htm) | (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsCancelled](5627aeaa-9d9c-dcbe-b34f-db40f1c025be.htm) | Indicates whether the event is being cancelled. (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A single event is an event that is not directly related to another event, meaning that there is no corresponding pre\-event or post\-event surrounding a single event. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Events Namespace](../ungrouped/Autodesk.-Revit.-DB.-Events-Namespace.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
System EventArgs 
[Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm) 
Autodesk.Revit.DB.Events RevitAPISingleEventArgs 
[Autodesk.Revit.DB.Events ApplicationInitializedEventArgs](a2cd37be-e16f-24ce-e100-8ae8c6588d73.htm) 
[Autodesk.Revit.DB.Events DocumentChangedEventArgs](8fd170b2-df48-209b-438e-54ec7b01b664.htm) 
[Autodesk.Revit.DB.Events DocumentWorksharingEnabledEventArgs](e8e6a008-e97e-ddc3-6ac1-f625e04ff314.htm) 
[Autodesk.Revit.DB.Events FailuresProcessingEventArgs](a35dc3de-c8a4-8af0-6a3c-706716e5f885.htm) 
[Autodesk.Revit.DB.Events ProgressChangedEventArgs](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm) 
[Autodesk.Revit.DB.Events WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.htm) 
[Autodesk.Revit.UI.Events DockableFrameFocusChangedEventArgs](1aa44a28-c45d-d77b-ced8-3b5cd5e582f3.htm) 
[Autodesk.Revit.UI.Events DockableFrameVisibilityChangedEventArgs](bc6bbc27-ed14-c79d-9e00-5c43b9cf978c.htm) 
[Autodesk.Revit.UI.Events ExternalDataManagerChangedEventArgs](2b1b09f9-3533-f7f3-062d-601899711f28.htm) 
[Autodesk.Revit.UI.Events FabricationPartBrowserChangedEventArgs](2af49738-a0c3-0e9b-f344-0f39d15dbd49.htm) 
[Autodesk.Revit.UI.Events MacroUpdatedEventArgs](a7504735-3c97-f5d4-a502-0195207364cc.htm) 
[Autodesk.Revit.UI.Events SelectionChangedEventArgs](8a744513-6de0-de55-c44c-bba00b949863.htm) 
[Autodesk.Revit.UI.Events ThemeChangedEventArgs](5525aa02-cbb1-145a-07ff-cccd62ef932d.htm) 
[Autodesk.Revit.UI.Events TransferredProjectStandardsEventArgs](e7e40805-bd07-4e96-ab10-0ed0fe6b3bfc.htm)
