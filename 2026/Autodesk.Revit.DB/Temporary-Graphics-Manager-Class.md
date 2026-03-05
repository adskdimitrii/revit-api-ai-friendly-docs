# Temporary Graphics Manager Class

Source: https://www.revitapidocs.com/2026/1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm

---

| Temporary Graphics Manager Class |
| --- |

A class that provides functionality to create temporary graphics in a Revit model. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB TemporaryGraphicsManager 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class TemporaryGraphicsManager : IDisposable
```

```
Public Class TemporaryGraphicsManager
	Implements IDisposable
```

```
public ref class TemporaryGraphicsManager : IDisposable
```

```
type TemporaryGraphicsManager = 
    class
        interface IDisposable
    end
```
The TemporaryGraphicsManager type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](57dd1d67-b10f-579c-27bd-59d2d79bb106.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddControl](dbe10b60-8a28-50b9-c7d5-91628e8fe630.htm) | Creates an in\-canvas control. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Clear](d1f91a81-eb1e-fc9e-de5d-cfcfdb359b10.htm) | Clear all temporary graphics objects managed by this manager. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](af31a45b-fb8d-b6ab-e57a-7e04f9645540.htm) | Releases all resources used by the TemporaryGraphicsManager |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAll](24142a59-8423-33da-9801-1792224379eb.htm) | Returns all temporary graphics object indexes managed by this manager. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetTemporaryGraphicsManager](208ba2b1-7658-c4eb-6a66-1d6a90878ccf.htm) | Gets a TemporaryGraphicsManager reference of the document. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [RemoveControl](3803b2b0-c688-faa3-ae1f-fdbd0135dd5a.htm) | Deletes the existing control identified by the unique index. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetTooltip](Temporary-Graphics-Manager-Set-Tooltip-Method.md) | Sets the tooltip for the temporary graphics object. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetVisibility](69d4d684-9774-b729-551d-aacede3f86b9.htm) | Changes the visibility of temporary graphics object. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [UpdateControl](eaf9c597-4b7f-7f92-c43c-0adebc5ef068.htm) | Updates the in\-canvas control identified by the unique index. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The graphics created by this class are temporary or transient. They are not subject to undo and are not saved. It's caller's
 responsiblity to manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
