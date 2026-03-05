# Parameter Utils Download Company Name Method

Source: https://www.revitapidocs.com/2026/a7c212e1-43a1-8bc4-f9be-0dcbf56b27c5.htm

---

| Parameter Utils Download Company Name Method |
| --- |

Downloads the name of the given parameter's owning account and records it in the given document. If the owning
 account's name is already recorded in the given document, this method returns the name without downloading it
 again. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string DownloadCompanyName(
	Document document,
	ForgeTypeId parameterTypeId
)
```

```
Public Shared Function DownloadCompanyName ( 
	document As Document,
	parameterTypeId As ForgeTypeId
) As String
```

```
public:
static String^ DownloadCompanyName(
	Document^ document, 
	ForgeTypeId^ parameterTypeId
)
```

```
static member DownloadCompanyName : 
        document : Document * 
        parameterTypeId : ForgeTypeId -> string 
```

#### Parameters

document [Document](Document-Class.md)
:   Document in which to record the name of the parameter's owning account.

parameterTypeId [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)
:   Parameter identifier.

#### Return Value

String 
Name of the owning account. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [AccessDeniedException](f280ddf5-9f59-eca8-634e-ace30de1f4bb.htm) | Thrown when the user is not authorized to access the requested information. |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the parameter identifier does not include an account identifier. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| \[!:Autodesk::Revit::Exceptions::NetworkCommunicationError] | Thrown when communication with the remote service is unsuccessful. |
| [ResourceNotFoundException](4ef7bcee-5831-e2c9-ee4a-06a0dd6c255f.htm) | Thrown when the requested information is not found |
| [ServerInternalException](dea21550-dd2d-e9d1-4f2f-5f18e0e58bc4.htm) | Thrown when the remote service reports an internal error. |
| [UnauthenticatedException](e94e82b6-4345-48ca-7be9-fd8393b0ff7f.htm) | Thrown when the user is not signed in. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks In Revit, the account name appears in the parameter tooltip if available. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ParameterUtils Class](Parameter-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
