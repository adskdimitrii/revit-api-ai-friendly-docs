# Parameter Utils Class

Source: https://www.revitapidocs.com/2026/df5da06e-35c6-e32e-53c0-9fd68d3ab142.htm

---

| Parameter Utils Class |
| --- |

A utility class of functions related to parameters. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB ParameterUtils 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static class ParameterUtils
```

```
Public NotInheritable Class ParameterUtils
```

```
public ref class ParameterUtils abstract sealed
```

```
[<AbstractClassAttribute>]
[<SealedAttribute>]
type ParameterUtils = class end
```
The ParameterUtils type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [DownloadCompanyName](Parameter-Utils-Download-Company-Name-Method.md) | Downloads the name of the given parameter's owning account and records it in the given document. If the owning  account's name is already recorded in the given document, this method returns the name without downloading it  again. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [DownloadParameter](6449c1fe-90af-e6d4-e852-91f6eeae5c97.htm) | Create a shared parameter element in the given document according to a parameter definition downloaded from the Parameters Service. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [DownloadParameterOptions](fd6683df-c93e-eabe-3f6c-dffe61b5cef9.htm) | Retrieves settings associated with the given parameter from the Parameters Service. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetAllBuiltInGroups](884d14d3-02e5-5631-adb3-79c612d04b5a.htm) | Gets the identifiers of all built\-in parameter groups. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetAllBuiltInParameters](bbcac12c-c02a-3747-55d0-95bc3f6d2bb2.htm) | Gets the identifiers of all built\-in parameters. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetBuiltInParameter](9b2b9b94-5220-0e9f-d259-c05faaf86625.htm) | Gets the BuiltInParameter value corresponding to built\-in parameter identified by the given ForgeTypeId. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetBuiltInParameterGroupTypeId](Parameter-Utils-Get-Built-In-Parameter-Group-Type-Id-Method.md) | The parameter group identifier corresponding to the given built\-in parameter identifier. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [GetParameterTypeId](7756d26f-c271-8259-b668-5e8eb888b29e.htm) | Gets the ForgeTypeId identifying the built\-in parameter corresponding to the given BuiltInParameter value. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsBuiltInGroup](50a42579-6e5e-7f9d-30ff-fdf41036c8e7.htm) | Checks whether a ForgeTypeId identifies a built\-in parameter group. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsBuiltInParameter(ElementId)](7df6bd75-52ac-3657-aef1-6d594809c6f9.htm) | Checks whether an ElementId identifies a built\-in parameter. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsBuiltInParameter(ForgeTypeId)](dd94c332-1755-910b-d3db-65ad9d396ce1.htm) | Checks whether a ForgeTypeId identifies a built\-in parameter. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
