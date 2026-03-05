# Import Instance Create(Document, View, External Resource Reference, SATImport Options, Link Load Result ) Method

Source: https://www.revitapidocs.com/2026/c8186d19-7c97-d4f9-972f-29c37a44c0a4.htm

---

| Import Instance Create(Document, View, External Resource Reference, SATImport Options, Link Load Result ) Method |
| --- |

Creates a new instance of SAT link type from an external resource reference
 and loads the linked file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ImportInstance Create(
	Document document,
	View DBView,
	ExternalResourceReference resourceReference,
	SATImportOptions options,
	out LinkLoadResult linkLoadResult
)
```

```
Public Shared Function Create ( 
	document As Document,
	DBView As View,
	resourceReference As ExternalResourceReference,
	options As SATImportOptions,
	<OutAttribute> ByRef linkLoadResult As LinkLoadResult
) As ImportInstance
```

```
public:
static ImportInstance^ Create(
	Document^ document, 
	View^ DBView, 
	ExternalResourceReference^ resourceReference, 
	SATImportOptions^ options, 
	[OutAttribute] LinkLoadResult^% linkLoadResult
)
```

```
static member Create : 
        document : Document * 
        DBView : View * 
        resourceReference : ExternalResourceReference * 
        options : SATImportOptions * 
        linkLoadResult : LinkLoadResult byref -> ImportInstance 
```

#### Parameters

document [Document](Document-Class.md)
:   The document in which to create the SAT link.

DBView [View](View-Class.md)
:   The view into which the SAT link will be created.

resourceReference [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)
:   The external resource reference describing the source of the DGN link.

options [SATImportOptions](ae7fbb19-3fdd-0f5e-6b11-a5301e134922.htm)
:   Various import options applicable to the SAT format.
 If , all options will be set to their respective default values.

linkLoadResult [LinkLoadResult](f846bfb0-b047-9332-567f-75ae880d8359.htm)
:   An object containing the results of creating and loading
 the SAT link. It contains the ElementId of the new created SAT link type.

#### Return Value

[ImportInstance](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm) 
The new instance of SAT link type created. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  document is in an edit mode.  \-or\-  Import is temporarily disabled.  \-or\-  The view is not printable.  \-or\-  ThisViewOnly cannot be true when importing a DWG\|DGN drawing into a 3D view.  \-or\-  One or more strings describing layer selection is invalid or empty.  \-or\-  The scale is not valid as a CustomScale for use during import.  \-or\-  The server referenced by the ExternalResourceReference does not exist or  does not implement IExternalResourceServer.  \-or\-  The server referenced by the ExternalResourceReference cannot support CAD links.  \-or\-  The ExternalResourceReference (resourceReference) is not in a format  that is supported by its server. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The Material Library is missing in the installed Revit.  \-or\-  The SAT Import/Link module is not available in the installed Revit. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This function creates a new SAT link type as well as a new instance of this SAT link type.
 The new instance of SAT link type is returned by this function and the element id of the new SAT link type
 is contained in the LinkLoadResult. 

If the given external resource reference of the DWG link is already used by an existing SAT link type,
 a new instance of this existing SAT link type is created and returned. The element id of the existing
 SAT link type is contained in the LinkLoadResult. 

This function regenerates the input document. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ImportInstance Class](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm) [Create Overload](ddb7b91a-482e-5cb6-edf6-913781024602.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
